# AI Tech Coffee Hours

A hands-on learning repository for understanding Large Language Model (LLM) fundamentals and AI agent development. This project provides interactive demonstrations of core LLM concepts through practical Azure OpenAI examples.

## 🎯 What You'll Learn

- **LLM Fundamentals**: Understanding stateless vs stateful interactions
- **Token Economics**: Real-time token usage tracking and cost awareness
- **Azure OpenAI Integration**: Practical API usage with the official SDK
- **Agent Development**: Building from primitives to frameworks

## 🚀 Quick Start

### Prerequisites
- Azure OpenAI account and deployment

### Install Python 3.12+

#### macOS
```bash
# Using Homebrew (recommended)
brew install python@3.12

# Or download from python.org
# Visit https://www.python.org/downloads/macos/
```

#### Windows
```bash
# Using winget (Windows 10+)
winget install Python.Python.3.12

# Or download from python.org
# Visit https://www.python.org/downloads/windows/
```

#### Linux (Ubuntu/Debian)
```bash
# Add deadsnakes PPA for latest Python versions
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-pip python3.12-venv

# Verify installation
python3.12 --version
```

#### Linux (CentOS/RHEL/Fedora)
```bash
# Fedora
sudo dnf install python3.12

# CentOS/RHEL (may need EPEL)
sudo yum install python3.12

# Or compile from source if not available in repos
```

### Install UV Package Manager

UV is a fast Python package installer and resolver. Install it with:

```bash
# Alternative: Install via pip
pip install uv

# Verify installation
uv --version
```

### Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/ai-tech-coffee-hours.git
   cd ai-tech-coffee-hours
   ```

2. **Verify Python and UV installation**:
   ```bash
   # Check Python version (should be 3.12+)
   python --version
   # or
   python3 --version
   
   # Check UV installation
   uv --version
   ```

3. **Create and activate a virtual environment using UV**:
   ```bash
   # Create virtual environment
   uv venv
   
   # Activate virtual environment
   # On macOS/Linux:
   source .venv/bin/activate
   
   # On Windows:
   # .venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

5. **Configure Azure OpenAI**:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI credentials
   ```

6. **Run the interactive learning session**:
   ```bash
   python main.py
   ```

## 🎮 Interactive Demonstrations

The main learning experience offers five modes:

### 1. Stateless Interactive Chat
Experience how LLMs work naturally - each conversation is independent with no memory between exchanges. Perfect for understanding the fundamental stateless nature of language models.

### 2. Stateless Chat with Context 
Learn how LLMs can answer questions based on provided context. This demo includes three fake Eminem-style rap songs:
- **"Heart on Fire"** - A love-themed song
- **"Rising from Ashes"** - About overcoming challenges
- **"Digital Dreams"** - Social media and technology critique

The LLM can answer questions about these songs while remaining stateless - demonstrating how context windows work without conversation memory.

### 3. Stateful Interactive Chat  
See how conversation history is preserved by explicitly sending context with each request. Watch how token usage grows as conversations get longer.

### 4. Chat with Tools (Function Calling)
Explore how LLMs can use external functions/tools like weather queries, time checks, and calculations.

### 5. Artisan Agent
Experience a decision-making loop that demonstrates higher-level agent capabilities.

### Token Usage Tracking
Every response shows real-time token consumption:
- **Input tokens**: Prompt + conversation history/context
- **Output tokens**: Assistant's response  
- **Total tokens**: Complete request cost

## 📚 Learning Sessions

### Session 1: LLM Primitives
- **Location**: `session_1/primitives/`
- **Focus**: Basic Azure OpenAI integration, stateless vs stateful concepts, and context understanding
- **Key Files**: 
  - `stateless_chat.py` - Basic stateless interactions
  - `stateless_chat_with_context.py` - Context-based Q&A demonstration
  - `stateful_chat.py` - Conversation history management
  - `tools_chat.py` - Function calling capabilities


## 🛠 Environment Variables

Create a `.env` file with your Azure OpenAI configuration:

```env
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

## 📁 Project Structure

```
ai-tech-coffee-hours/
├── session_1/
│   ├── primitives/
│   │   ├── shared_utils.py               # Azure OpenAI client utilities
│   │   ├── stateless_chat.py             # Basic stateless chat
│   │   ├── stateless_chat_with_context.py # Context-based Q&A
│   │   ├── stateful_chat.py              # Chat with conversation history
│   │   └── tools_chat.py                  # Function calling demo
│   └── framework/
│       ├── agent_framework.py             # Framework abstractions (planned)
│       └── artisan_agent.py               # Decision-making agent
├── .env.example                           # Environment template
├── pyproject.toml                         # Dependencies and project config
└── main.py                                # Interactive menu entry point
```

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.