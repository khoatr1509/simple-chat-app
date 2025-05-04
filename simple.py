from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

def main():
        # Load environment variables from .env file
        load_dotenv()

        # Initialize the model
        model = init_chat_model("claude-3-5-sonnet-latest", model_provider="anthropic")

        # Create simple messages
        system_message = SystemMessage("You are a helpful AI assistant.")
        human_message = HumanMessage("Hello, how are you today?")

        # Create a list of messages
        messages = [system_message, human_message]

        # Get response from the model
        response = model.invoke(messages)

        # Print the response
        print(response.content)
            