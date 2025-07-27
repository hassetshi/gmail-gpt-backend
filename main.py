from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from openai import OpenAI

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    print("❌ API key not found.")
else:
    print("🔑 Loaded Key:", api_key[:6] + "..." + api_key[-4:])
print("📌 Model to use:", "deepseek/deepseek-r1:free")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

@app.post("/summarize-emails")
async def summarize_emails(request: Request):
    body = await request.json()
    email_text = body.get("emails", "")

    prompt = f"Summarize the following emails:\n\n{email_text}"

    response = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": "Summarize these emails professionally."},
            {"role": "user", "content": prompt}
        ]
    )

    return {"summary": response.choices[0].message.content}
