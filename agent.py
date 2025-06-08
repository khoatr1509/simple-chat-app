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
    """Brief description of what this function does."""
    city = city.lower()
    if city in WEATHER_DATA:
        return WEATHER_DATA[city]
    else:
        return {"error": f"No weather data available for {city}"}

model = ChatAnthropic(model_name="claude-3-haiku-20240307")
tools = [get_weather]

agent_executor = create_react_agent(model, tools)

def print_agent_response(response):
    for message in response["messages"]:
        if hasattr(message, "pretty_print"):
            message.pretty_print()
        else:
            print(f"{type(message).__name__}: {message.content}")

system_message = SystemMessage(content="""You are a helpful assistant that can answer general knowledge questions and provide weather information.

When a user asks about weather but doesn't specify a location, politely ask them which city they're interested in.
When you have the city, use the get_weather tool to retrieve weather information.
For general knowledge questions, answer directly without using tools.

Be conversational and friendly in your responses.""")

print("\n=== General Knowledge Query ===\n")
response1 = agent_executor.invoke(
    {"messages": [system_message, HumanMessage(content="What is the capital of France?")]}
)
print_agent_response(response1)

print("\n=== Weather Query ===\n")
response2 = agent_executor.invoke(
    {"messages": [system_message, HumanMessage(content="What's the weather like in Paris?")]}
)
print_agent_response(response2)