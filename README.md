# AI Tech Coffee Hours

A hands-on learning repository for understanding Large Language Model (LLM) fundamentals and AI agent development. This project provides interactive demonstrations of core LLM concepts through practical Azure OpenAI examples.

## 🎯 What You'll Learn

- **LLM Fundamentals**: Understanding stateless vs stateful interactions
- **Token Economics**: Real-time token usage tracking and cost awareness
- **Azure OpenAI Integration**: Practical API usage with the official SDK
- **Agent Development**: Building from primitives to frameworks

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- UV package manager
- Azure OpenAI account and deployment

### Setup

1. **Install dependencies**:
   ```bash
   uv pip install -e .
   ```

2. **Configure Azure OpenAI**:
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI credentials
   ```

3. **Run the interactive learning session**:
   ```bash
   python session_1/primitives/agent_primitives.py
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