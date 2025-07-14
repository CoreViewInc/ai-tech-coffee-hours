from session_1.primitives.stateless_chat import demonstrate_stateless_chat
from session_1.primitives.stateful_chat import demonstrate_stateful_chat
from session_1.primitives.tools_chat import demonstrate_tools_chat
from session_1.primitives.artisan_agent import demonstrate_artisan_agent

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
║                     Learning LLM Fundamentals                               ║
║                     Session 1: Primitives                                   ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
    """)
    print("Choose what you want to demonstrate:")
    print("1. Stateless Interactive Chat (no memory between calls)")
    print("2. Stateful Interactive Chat (with conversation history)")
    print("3. Chat with Tools (Function Calling)")
    print("4. Artisan Agent (Decision-making loop)")
    print("5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            demonstrate_stateless_chat()
            print("\n" + "-" * 50)
            
        elif choice == "2":
            demonstrate_stateful_chat()
            print("\n" + "-" * 50)
            
        elif choice == "3":
            demonstrate_tools_chat()
            print("\n" + "-" * 50)
            
        elif choice == "4":
            demonstrate_artisan_agent()
            print("\n" + "-" * 50)
            
        elif choice == "5":
            print("Thanks for learning about LLMs! 👋")
            break
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        
        # Ask if they want to try something else
        if choice in ["1", "2", "3", "4"]:
            try_again = input("\nWould you like to try another demonstration? (y/n): ").strip().lower()
            if try_again != 'y' and try_again != 'yes':
                print("Thanks for learning about LLMs! 👋")
                break

if __name__ == "__main__":
    main()
