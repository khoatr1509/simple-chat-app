from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables from .env file
load_dotenv()

# Initialize the model
model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")

# Initialize a list to store conversation history
conversation_memory = []

# Add system message to memory
system_message = SystemMessage("You are a helpful AI assistant.")
conversation_memory.append(system_message)

# Function to add user message and get AI response
def get_ai_response(user_input):
    # Add user message to memory
    user_message = HumanMessage(user_input)
    conversation_memory.append(user_message)
    
    # Get response from model
    response = model.invoke(conversation_memory)
    
    # Add AI response to memory
    conversation_memory.append(response)
    
    return response.content

# Example usage
print("AI Assistant is ready. Type 'exit' to end the conversation.")
while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    
    ai_response = get_ai_response(user_input)
    print(f"AI: {ai_response}")

# Print conversation history
print("\nConversation History:")
for message in conversation_memory:
    if isinstance(message, SystemMessage):
        print(f"System: {message.content}")
    elif isinstance(message, HumanMessage):
        print(f"User: {message.content}")
    elif isinstance(message, AIMessage):
        print(f"AI: {message.content}")