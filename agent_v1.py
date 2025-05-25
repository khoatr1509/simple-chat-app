from dotenv import load_dotenv
from typing import Dict, Any
from langchain_anthropic import ChatAnthropic
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

# Load environment variables from .env file
load_dotenv()

# Mock weather data
WEATHER_DATA = {
    "new york": {"temperature": 72, "condition": "Partly Cloudy", "humidity": 65},
    "london": {"temperature": 58, "condition": "Rainy", "humidity": 80},
    "tokyo": {"temperature": 79, "condition": "Sunny", "humidity": 45},
    "sydney": {"temperature": 68, "condition": "Cloudy", "humidity": 60},
    "paris": {"temperature": 66, "condition": "Clear", "humidity": 50},
}

@tool
def get_weather(city: str) -> Dict[str, Any]:
    """Get current weather conditions for a specific city."""
    city = city.lower()
    if city in WEATHER_DATA:
        return WEATHER_DATA[city]
    else:
        return {"error": f"No weather data available for {city}"}

# Create the model and tools
model = ChatAnthropic(model_name="claude-3-haiku-20240307")
tools = [get_weather]

# Create a system message that instructs the agent to ask about location for weather queries
system_message = SystemMessage(content="""You are a helpful assistant that can answer general knowledge questions and provide weather information.
You must first start with greeting message "Hello, I will help you check the weather at your location"
When a user asks about weather but doesn't specify a location, politely ask them which city they're interested in.
When you have the city, use the get_weather tool to retrieve weather information.
For general knowledge questions, answer directly without using tools.

Be conversational and friendly in your responses.""")

# Create the agent
agent_executor = create_react_agent(model, tools)

# Run an interactive chat loop
def interactive_chat():
    print("Weather Assistant Chat")
    print("======================")
    print("Type 'exit' to end the conversation")
    
    user_input = ""
    # Initialize conversation with just the system message
    messages_list = [system_message]
    messages_list.append(HumanMessage(content="Start agent"))
    while True:
        # Invoke the agent with all messages in the list
        response = agent_executor.invoke({"messages": messages_list})
        
        # Extract the latest assistant message
        assistant_message = response["messages"][-1]
        
        # Add the assistant message to our list
        messages_list.append(assistant_message)
        
        # Print the assistant response
        print(f"Assistant: {assistant_message.content}")
        
        user_input = input("\nYou: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Assistant: Goodbye! Have a great day!")
            break
        
        # Add the human message to our simple list
        messages_list.append(HumanMessage(content=user_input))
        

# Start the interactive chat
if __name__ == "__main__":
    interactive_chat()