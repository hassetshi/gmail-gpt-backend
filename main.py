from fastapi import FastAPI
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

print("Loaded API Key:", os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"  # OpenRouter URL
)

@app.get("/summarize-emails")
def summarize_emails():
    emails = """
    1. John requested a price update for the Q3 proposal.
    2. HR sent a reminder about the upcoming performance reviews.
    3. Jane submitted the blog draft for approval.
    """
    prompt = f"Summarize the following emails:\n\n{emails}"

    response = client.chat.completions.create(
        model="deepseek-chat",  # or try "openai/gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "Summarize these emails professionally."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"summary": response.choices[0].message.content}
