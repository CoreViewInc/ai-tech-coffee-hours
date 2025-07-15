import os
import json
from datetime import datetime
import random
from session_1.primitives.shared_utils import create_azure_openai_client

# Define simple example functions to demonstrate tool calling
def get_current_weather(location: str, unit: str = "celsius"):
    """Get the current weather for a given location"""
    # Simulated weather data for demonstration
    weather_conditions = ["sunny", "cloudy", "rainy", "snowy"]
    temp = random.randint(-10, 35) if unit == "celsius" else random.randint(14, 95)
    
    return json.dumps({
        "location": location,
        "temperature": temp,
        "unit": unit,
        "condition": random.choice(weather_conditions),
        "humidity": random.randint(30, 80),
        "wind_speed": random.randint(5, 30)
    })


# Define the tools schema for OpenAI
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

# Map function names to actual functions
available_functions = {
    "get_current_weather": get_current_weather,
}

def demonstrate_tools_chat():
    """
    Interactive chat demonstration with function calling (tools).
    Shows how the model can use tools to answer questions.
    Type 'quit' to exit.
    """
    print("\n" + "="*60)
    print("CHAT WITH TOOLS DEMONSTRATION")
    print("The assistant can use tools to get weather")
    print("Try asking: 'What's the weather in Paris?'")
    print("Type 'quit' to exit")
    print("="*60 + "\n")
    
    client = create_azure_openai_client()
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    
    # Initialize conversation with system prompt
    messages = [
        {"role": "system", "content": "You are a helpful assistant with access to tools. Use them when needed to answer questions accurately."}
    ]
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})
        
        try:
            # Send request with tools enabled
            response = client.chat.completions.create(
                model=deployment_name,
                messages=messages,
                tools=tools,
                tool_choice="auto",  # Let the model decide when to use tools
                temperature=0.7
            )
            
            response_message = response.choices[0].message
            tool_calls = response_message.tool_calls
            
            # Check if the model wantgs to use a tool
            if tool_calls:
                # Add the assistant's response to messages
                messages.append(response_message)
                
                print(f"🔧 Assistant is using tools...")
                
                # Process each tool call
                for tool_call in tool_calls:
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    print(f"   → Calling {function_name} with args: {function_args}")
                    
                    # Call the function
                    function_to_call = available_functions[function_name]
                    function_response = function_to_call(**function_args)
                    
                    # Add the function response to messages
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response,
                    })
                
                # Get a new response from the model with the function results
                second_response = client.chat.completions.create(
                    model=deployment_name,
                    messages=messages,
                    temperature=0.7
                )
                
                final_message = second_response.choices[0].message.content
                usage = second_response.usage
                
                print(f"\nAssistant: {final_message}")
                print(f"📊 Tokens - Input: {usage.prompt_tokens}, Output: {usage.completion_tokens}, Total: {usage.total_tokens}")
                
                # Add final response to conversation history
                messages.append({"role": "assistant", "content": final_message})
                
            else:
                # No tool was called, just a regular response
                assistant_message = response_message.content
                usage = response.usage
                
                print(f"Assistant: {assistant_message}")
                print(f"📊 Tokens - Input: {usage.prompt_tokens}, Output: {usage.completion_tokens}, Total: {usage.total_tokens}")
                
                # Add assistant's response to conversation history
                messages.append({"role": "assistant", "content": assistant_message})
            
        except Exception as e:
            print(f"Error: {e}")
            break
    
    print("\n✅ The assistant successfully used tools to answer your questions!")

if __name__ == "__main__":
    demonstrate_tools_chat()