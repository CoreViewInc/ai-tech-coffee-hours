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
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

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

3. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

4. **Configure Azure OpenAI**:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI credentials
   ```

5. **Run the interactive learning session**:
   ```bash
   python main.py
   ```

## 🎮 Interactive Demonstrations

The main learning experience offers three modes:

### 1. Stateless Interactive Chat
Experience how LLMs work naturally - each conversation is independent with no memory between exchanges. Perfect for understanding the fundamental stateless nature of language models.

### 2. Stateful Interactive Chat  
See how conversation history is preserved by explicitly sending context with each request. Watch how token usage grows as conversations get longer.

### 3. Token Usage Tracking
Every response shows real-time token consumption:
- **Input tokens**: Prompt + conversation history
- **Output tokens**: Assistant's response  
- **Total tokens**: Complete request cost

## 📚 Learning Sessions

### Session 1: LLM Primitives
- **Location**: `session_1/primitives/`
- **Focus**: Basic Azure OpenAI integration and stateless vs stateful concepts
- **Key File**: `agent_primitives.py` - Interactive demonstrations

### Future Sessions
- Agent frameworks and abstractions
- Advanced conversation management
- Multi-agent systems

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
│   │   └── agent_primitives.py    # Interactive LLM demonstrations
│   └── framework/
│       ├── agent_framework.py     # Framework abstractions (planned)
│       └── artisan_agent.py       # Specialized agents (planned)
├── .env.example                   # Environment template
├── pyproject.toml                 # Dependencies and project config
└── main.py                        # Basic entry point
```

## 🎓 Educational Goals

This repository is designed for:
- **Understanding LLM fundamentals** through hands-on interaction
- **Learning token economics** and cost management
- **Building practical experience** with Azure OpenAI
- **Progressive skill development** from primitives to frameworks

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.