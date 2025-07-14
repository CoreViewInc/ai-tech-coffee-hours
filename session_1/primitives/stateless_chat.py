import os
from session_1.primitives.shared_utils import create_azure_openai_client, single_chat_completion

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

if __name__ == "__main__":
    demonstrate_stateless_chat()