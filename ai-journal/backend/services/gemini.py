import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

async def process_entry(content: str) -> tuple[str, str]:
    # Generate summary
    summary_prompt = f"Please provide a concise summary of the following journal entry: {content}"
    summary_response = model.generate_content(summary_prompt)
    summary = summary_response.text

    # Generate mood tag
    mood_prompt = f"Based on this journal entry, suggest a single word mood tag: {content}"
    mood_response = model.generate_content(mood_prompt)
    mood_tag = mood_response.text.strip().lower()

    return summary, mood_tag 