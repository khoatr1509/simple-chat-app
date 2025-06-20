from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain.chat_models import init_chat_model

app = FastAPI()

app.mount("/chat_app/static", StaticFiles(directory="chat_app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_index():
    with open("chat_app/static/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)

class ChatRequest(BaseModel):
    message: str

# 🔹 Global history list (shared by all users)
chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

@app.post("/chat")
def chat(request: ChatRequest):
    load_dotenv()

    model = init_chat_model("claude-sonnet-4-20250514", model_provider="anthropic")

    # Add the new user message
    chat_history.append(HumanMessage(content=request.message))

    # Call the model with full history
    response = model.invoke(chat_history)

    # Append model response to history
    chat_history.append(AIMessage(content=response.content))

    return {
        "response": response.content,
        "history": [{"role": m.type, "content": m.content} for m in chat_history]
    }
