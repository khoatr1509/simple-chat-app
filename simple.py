from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

def main():
        # Load environment variables from .env file
        load_dotenv()

        # Initialize the model
        model = init_chat_model("claude-3-haiku-20240307", model_provider="anthropic")
        
        # Create simple messages
        system_message = SystemMessage("You are a helpful AI assistant you need to follow strictly the documents content.")
        human_message = HumanMessage("Write 10 random words about Harry Potter")

        # Create a list of messages
        messages = [system_message, human_message]

        # Get response from the model
        response = model.invoke(messages)

        # Print the response
        print(response.content)

main()