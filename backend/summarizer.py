import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None

async def get_ai_summary(text: str) -> str:
    if not client:
        return "Error: API_KEY is missing. Please check your .env file."
    
    # Strict 20% to 30% compression constraint
    prompt_instruction = (
        "You are an expert master summarizer. Distill the given text down to its essential core.\n\n"
        "Strict Rules:\n"
        "1. LENGTH: The final summary must be strictly **20% to 30% of the original text's length** (a high-precision, concise reduction that cuts out all fluff and repetition).\n"
        "2. STYLE: Keep it extremely precise, simple, clear, and strictly to the point.\n"
        "3. LANGUAGE: Match the input language completely (clean, natural wording).\n"
        "4. FORMAT: Provide ONLY the summary text. No bullet points, no headings, no introductory or concluding filler.\n\n"
        f"Original Text:\n{text}"
    )
    
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt_instruction,
        )
        return response.text
    except Exception as e:
        return f"Backend API Error: {str(e)}"
