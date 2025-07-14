import os
from session_1.primitives.shared_utils import create_azure_openai_client

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

if __name__ == "__main__":
    demonstrate_stateful_chat()