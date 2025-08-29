from session_1.primitives.stateless_chat import demonstrate_stateless_chat
from session_1.primitives.stateless_chat_with_context import demonstrate_stateless_chat_with_context
from session_1.primitives.stateful_chat import demonstrate_stateful_chat
from session_1.primitives.tools_chat import demonstrate_tools_chat
from session_1.primitives.artisan_agent import demonstrate_artisan_agent
from session_2.rag.rag_agent import demonstrate_rag_agent
from session_2.rag.importer import main as importer_main

def main():
    """
    Main function with menu to choose what demonstration to run.
    Shows different Azure OpenAI capabilities and LLM fundamentals.
    """
    print("""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║   ██████╗ ██████╗ ██████╗ ███████╗██╗   ██╗██╗███████╗██╗    ██╗            ║
║  ██╔════╝██╔═══██╗██╔══██╗██╔════╝██║   ██║██║██╔════╝██║    ██║            ║
║  ██║     ██║   ██║██████╔╝█████╗  ██║   ██║██║█████╗  ██║ █╗ ██║            ║
║  ██║     ██║   ██║██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██╔══╝  ██║███╗██║            ║
║  ╚██████╗╚██████╔╝██║  ██║███████╗ ╚████╔╝ ██║███████╗╚███╔███╔╝            ║
║   ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝             ║
║                                                                             ║
║                        AI Tech Coffee Hour                                  ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
    """)
    print("Choose what you want to demonstrate:")
    print("")
    print("*** Session 1 - Primitives ***")
    print("1. Stateless Interactive Chat (no memory between calls)")
    print("2. Stateless Chat with Context (Eminem songs demo)")
    print("3. Stateful Interactive Chat (with conversation history)")
    print("4. Chat with Tools (Function Calling)")
    print("5. Artisan Agent (Decision-making loop)")
    print("")
    print("*** Session 2 - RAG ***")
    print("6. Import Data to Qdrant (./data → session2_rag)")
    print("7. RAG Agent (Retriever tool)")
    print("")
    print("8. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == "1":
            demonstrate_stateless_chat()
            print("\n" + "-" * 50)
            
        elif choice == "2":
            demonstrate_stateless_chat_with_context()
            print("\n" + "-" * 50)
            
        elif choice == "3":
            demonstrate_stateful_chat()
            print("\n" + "-" * 50)
            
        elif choice == "4":
            demonstrate_tools_chat()
            print("\n" + "-" * 50)
            
        elif choice == "5":
            demonstrate_artisan_agent()
            print("\n" + "-" * 50)
            
        elif choice == "6":
            print("\nImporting data from ./data to Qdrant (collection: session2_rag)...")
            importer_main()
            print("\n" + "-" * 50)

        elif choice == "7":
            demonstrate_rag_agent()
            print("\n" + "-" * 50)

        elif choice == "8":
            print("Thanks for learning about LLMs! 👋")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
        
        # Ask if they want to try something else
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            try_again = input("\nWould you like to try another demonstration? (y/n): ").strip().lower()
            if try_again != 'y' and try_again != 'yes':
                print("Thanks for learning about LLMs! 👋")
                break

if __name__ == "__main__":
    main()
