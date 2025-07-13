import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_azure_openai_client():
    """
    Creates and returns an Azure OpenAI client instance.
    Requires the following environment variables:
    - AZURE_OPENAI_API_KEY
    - AZURE_OPENAI_ENDPOINT
    - AZURE_OPENAI_API_VERSION
    """
    client = AzureOpenAI(
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4.1"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )
    return client

def single_chat_completion(client, deployment_name, system_prompt, user_message):
    """
    Helper function that makes a single chat completion call.
    Used by both stateless and stateful chat demonstrations.
    Returns tuple: (response_text, usage_info)
    """
    try:
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        
        response_text = response.choices[0].message.content
        usage = response.usage
        usage_info = {
            "input_tokens": usage.prompt_tokens,
            "output_tokens": usage.completion_tokens,
            "total_tokens": usage.total_tokens
        }
        
        return response_text, usage_info
    except Exception as e:
        print(f"Error calling Azure OpenAI: {e}")
        return None, None

def demonstrate_stateless_chat():
    """
    Interactive STATELESS chat demonstration.
    Each call is independent - the model has no memory of previous interactions.
    Type 'quit' to exit.
    """
    print("\n" + "="*60)
    print("STATELESS CHAT DEMONSTRATION")
    print("Each call is independent - no memory between calls")
    print("Type 'quit' to exit")
    print("="*60 + "\n")
    
    client = create_azure_openai_client()
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    
    system_prompt = "You are a helpful assistant who loves to help with learning."
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Make a fresh call every time - NO conversation history
        response, usage = single_chat_completion(client, deployment_name, system_prompt, user_input)
        if response:
            print(f"Assistant: {response}")
            print(f"📊 Tokens - Input: {usage['input_tokens']}, Output: {usage['output_tokens']}, Total: {usage['total_tokens']}")
        else:
            print("Error getting response. Try again or type 'quit' to exit.")
    
    print("\n⚠️  Notice: In this mode, the assistant never remembers what you said before!")

def demonstrate_stateful_chat():
    """
    Interactive STATEFUL chat demonstration.
    Conversation history is preserved - the model remembers context.
    Type 'quit' to exit.
    """
    print("\n" + "="*60)
    print("STATEFUL CHAT DEMONSTRATION")
    print("Conversation history is preserved - the model remembers context")
    print("Type 'quit' to exit")
    print("="*60 + "\n")
    
    client = create_azure_openai_client()
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    
    # Initialize conversation with system prompt
    messages = [
        {"role": "system", "content": "You are a helpful assistant who loves to help with learning."}
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
            # Send entire conversation history with each request
            response = client.chat.completions.create(
                model=deployment_name,
                messages=messages,
                temperature=0.7
            )
            
            # Extract assistant's response and usage info
            assistant_message = response.choices[0].message.content
            usage = response.usage
            
            print(f"Assistant: {assistant_message}")
            print(f"📊 Tokens - Input: {usage.prompt_tokens}, Output: {usage.completion_tokens}, Total: {usage.total_tokens}")
            
            # Add assistant's response to conversation history
            messages.append({"role": "assistant", "content": assistant_message})
            
        except Exception as e:
            print(f"Error: {e}")
            break
    
    print("\n✅ Notice: In this mode, the assistant remembers everything from your conversation!")


def main():
    """
    Main function with menu to choose what demonstration to run.
    Shows the differences between stateless and stateful LLM interactions.
    """
    print("🤖 Azure OpenAI Learning Session")
    print("=" * 50)
    print("Choose what you want to demonstrate:")
    print("1. Stateless Interactive Chat (no memory between calls)")
    print("2. Stateful Interactive Chat (with conversation history)")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            demonstrate_stateless_chat()
            print("\n" + "-" * 50)
            
        elif choice == "2":
            demonstrate_stateful_chat()
            print("\n" + "-" * 50)
            
        elif choice == "3":
            print("Thanks for learning about LLMs! 👋")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")
        
        # Ask if they want to try something else
        try_again = input("\nWould you like to try another demonstration? (y/n): ").strip().lower()
        if try_again != 'y' and try_again != 'yes':
            print("Thanks for learning about LLMs! 👋")
            break

if __name__ == "__main__":
    main()