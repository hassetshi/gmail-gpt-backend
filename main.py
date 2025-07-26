
from fastapi import FastAPI
from openai import OpenAI
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/summarize-emails")
def summarize_emails():
    emails = '''
    1. John requested a price update for the Q3 proposal.
    2. HR sent a reminder about the upcoming performance reviews.
    3. Jane submitted the blog draft for approval.
    '''
    prompt = f"Summarize the following emails:\n\n{emails}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize these emails professionally."},
            {"role": "user", "content": prompt}
        ]
    )
    summary = response.choices[0].message.content
    return {"summary": summary}
