from typing import Dict, Any, Union
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

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