
from fastapi import FastAPI
from openai import OpenAI  # works with DeepSeek too
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

client = OpenAI(
   api_key=os.getenv("DEEPSEEK_API_KEY"),
   base_url="https://api.deepseek.com/v1"  # use DeepSeek endpoint
)

@app.get("/summarize-emails")
def summarize_emails():
    emails = """
    1. John requested a price update...
    2. HR sent a reminder...
    3. Jane submitted the blog draft...
    """
    response = client.chat.completions.create(
        model="deepseek-chat",  # or "deepseek-reasoner"
        messages=[
            {"role": "system", "content": "Summarize these emails carefully."},
            {"role": "user", "content": emails}
        ]
    )
    return {"summary": response.choices[0].message.content}

