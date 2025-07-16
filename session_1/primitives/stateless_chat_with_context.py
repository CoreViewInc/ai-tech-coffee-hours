import os
from session_1.primitives.shared_utils import create_azure_openai_client, single_chat_completion

def demonstrate_stateless_chat_with_context():
    """
    Interactive STATELESS chat demonstration with context.
    Shows how LLMs can answer questions based on provided context (fake Eminem songs).
    Each call is independent but includes the same context.
    Type 'quit' to exit.
    """
    print("\n" + "="*60)
    print("STATELESS CHAT WITH CONTEXT DEMONSTRATION")
    print("Ask questions about the three Eminem songs below")
    print("Each call is independent but includes song context")
    print("Type 'quit' to exit")
    print("="*60 + "\n")
    
    # Create fake Eminem songs for context
    fake_songs_context = """
Here are three Eminem songs from his latest album:

Song 1: "Heart on Fire"
Verse: My heart's ablaze, can't contain this feeling inside
       Love hit me like a tidal wave, nowhere to hide
       She's my sunrise, my moonlight, my everything true
       Never thought I'd find someone who makes me feel brand new

Song 2: "Rising from Ashes"
Verse: Started from the bottom, now I'm climbing every day
       Life knocked me down a thousand times, but I found my way
       Every scar's a lesson, every fall made me strong
       Now I'm standing tall, proving all the doubters wrong

Song 3: "Digital Dreams"
Verse: Living in a world of screens, reality's getting blurred
       Social media's got us trapped, truth is rarely heard
       Chasing likes and follows, but what's it really worth?
       Time to disconnect and find what matters here on Earth
"""
    
    print("🎵 FAKE EMINEM SONGS CONTEXT:")
    print("\nNow you can ask questions about these songs!")
    print("Example: 'Which song talks about love?'")
    print("Example: 'What's the theme of Digital Dreams?'")
    print("Example: 'Which song is about overcoming challenges?'\n")
    
    client = create_azure_openai_client()
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    
    # System prompt includes the context about the fake songs
    system_prompt = f"""You are a helpful music expert assistant. You have knowledge about these specific Eminem songs:

{fake_songs_context}

When users ask questions about Eminem's songs, answer based ONLY on the three songs provided above. 
Be specific and reference the actual lyrics or themes from these songs.
If asked about songs not in this list, politely say you only have information about these three songs."""
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Make a fresh call every time - NO conversation history
        # But the system prompt always includes the song context
        response, usage = single_chat_completion(client, deployment_name, system_prompt, user_input)
        if response:
            print(f"\nAssistant: {response}")
            print(f"\n📊 Tokens - Input: {usage['input_tokens']}, Output: {usage['output_tokens']}, Total: {usage['total_tokens']}")
        else:
            print("Error getting response. Try again or type 'quit' to exit.")
    

if __name__ == "__main__":
    demonstrate_stateless_chat_with_context()