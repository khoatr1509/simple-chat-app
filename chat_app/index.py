from typing import Dict, Any, Union
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from fastapi import FastAPI

app = FastAPI()

app.mount("/chat_app/static", StaticFiles(directory="chat_app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("chat_app/static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
     # Load environment variables from .env file
    load_dotenv()

    # Initialize the model
    model = init_chat_model("claude-3-haiku-20240307", model_provider="anthropic")
    message = request.message
    # Create simple messages
    system_message = SystemMessage("You are a helpful AI assistant you need to follow strictly the documents content.")
    human_message = HumanMessage(message)

    # Create a list of messages
    messages = [system_message, human_message]

    # Get response from the model
    response = model.invoke(messages)

    return {
        "response": response.content
    }