import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None

async def get_ai_summary(text: str) -> str:
    if not client:
        return "Error: API_KEY is missing. Please check your .env file."
    
    # Balanced length constraint: Just slightly shorter than the original, not too compressed
    prompt_instruction = (
        "You are an expert human editor. Summarize the following text naturally and fluidly.\n\n"
        "Strict Rules:\n"
        "1. Flow & Tone: Write a smooth, well-crafted paragraph in a natural tone.\n"
        "2. Balanced Length: Make it **just slightly shorter** than the original text (trim away minor fluff, but keep all core context and details intact). Avoid making it a single abrupt line.\n"
        "3. Language: Match the language of the input text completely (keep the easy wording and natural flow).\n"
        "4. Strict Formatting: Provide ONLY the summary text. No bullet points, no headings, and no introductory filler.\n\n"
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
