# fastapi_app.py
from fastapi import FastAPI
from pydantic import BaseModel
import os
from mistralai import Mistral
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key = os.getenv('MISTRAL_API_KEY')

model = "mistral-large-2407"


# client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
client = Mistral(api_key=api_key)

# model = "mistral-large-2407"

# client = Mistral(api_key=api_key)

class UserRequest(BaseModel):
    text: str

def mistral_api_call(messages):
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=messages,
            temperature=0.9,    # Higher temperature for more creative responses
            max_tokens=150,     # Increased slightly for more complete responses
            top_p=0.95          # Slightly higher top_p for more varied vocabulary
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        error_message = str(e)
        if "429" in error_message:
            return "😅 Oops! I'm a bit overwhelmed right now. Could you try again in a moment? I promise I'll be ready with a witty response!"
        else:
            return f"😕 Something went wrong on my end. Error: {error_message}"




@app.post("/predict_emoji")
async def predict_emoji(user_request: UserRequest):
    messages = [
        {"role": "system", "content": "You are an emoji expert. Respond with only a single emoji that best matches the emotion or theme of the text."},
        {"role": "user", "content": user_request.text}
    ]
    return {"emoji": mistral_api_call(messages)}

@app.post("/generate_response")
async def generate_response(user_request: UserRequest):
    emoji = await predict_emoji(user_request)
    messages = [
        {"role": "system", "content": "You are Emojinator, a witty and sarcastic chatbot with a great sense of humor. Your responses should be clever, playful, and sometimes use puns. Keep responses concise but impactful."},
        {"role": "user", "content": f"Make a witty response to this, using the emoji {emoji['emoji']}: {user_request.text}"}
    ]
    response = mistral_api_call(messages)
    return {"response": response, "emoji": emoji["emoji"]}

@app.get("/")
async def main():
    return {"message": "Hello World"}

# # @app.post("/")
# async def root():
#     return {"message": "Hello World"}
