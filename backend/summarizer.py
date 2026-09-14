import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY) if API_KEY else None

async def get_ai_summary(text: str) -> str:
    if not client:
        return "Error: API_KEY is missing. Please check your .env file."
    
    # Let the AI breathe: Focus on natural flow, clear context, and organic brevity
    prompt_instruction = (
        "You are an expert human editor. Summarize the following text naturally and fluidly.\n\n"
        "Rules for the summary:\n"
        "1. Flow & Tone: Write a single, well-crafted paragraph that reads naturally. Do NOT sound robotic or disjointed.\n"
        "2. Vocabulary: Use clear, everyday language that is easy to understand, but absolutely maintain the core meaning, context, and nuance of the original text.\n"
        "3. Organic Length: Keep it concise (roughly 10% to 15% of the original). If the input text is very short, write a natural 2-3 sentence summary that actually explains the point rather than cutting it off abruptly.\n"
        "4. Strict Formatting: Provide ONLY the summary text. No labels, no bullet points, no introductory fluff like 'Here is a summary'.\n\n"
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
