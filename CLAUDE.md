# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI Tech Coffee Hours learning repository focused on demonstrating LLM fundamentals and agent framework development. The project is organized into sessions that build upon each other to teach AI/LLM concepts through hands-on examples.

## Environment and Dependencies

- **Python Version**: 3.12+
- **Package Manager**: UV (not pip)
- **Dependencies**: Managed via `pyproject.toml`

### Setup Commands
```bash
# Install dependencies
uv pip install -e .

# Create environment file (copy from template)
cp .env.example .env
# Then edit .env with your Azure OpenAI credentials
```

## Environment Variables Required

The project requires Azure OpenAI configuration in a `.env` file:
```
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
```

## Running the Code

### Main Learning Session
```bash
# Run the interactive LLM demonstration
python main.py
```

This launches an interactive menu with four modes:
1. **Stateless Interactive Chat** - Demonstrates LLM statelessness (no memory between calls)
2. **Stateful Interactive Chat** - Shows conversation history preservation
3. **Chat with Tools (Function Calling)** - Demonstrates how LLMs can use functions/tools
4. **Exit**

### Individual Components
You can also run each component separately:
```bash
# Run stateless chat demo
python session_1/primitives/stateless_chat.py

# Run stateful chat demo
python session_1/primitives/stateful_chat.py

# Run tools/function calling demo
python session_1/primitives/tools_chat.py
```

## Architecture

### Session-Based Learning Structure
- **`session_1/`**: Foundation concepts
  - **`primitives/`**: Basic LLM interaction patterns
    - `shared_utils.py`: Shared utilities for Azure OpenAI client creation
    - `stateless_chat.py`: Demonstrates stateless LLM interactions (no memory)
    - `stateful_chat.py`: Demonstrates stateful LLM interactions (with conversation history)
    - `tools_chat.py`: Demonstrates function calling/tools capability
  - **`framework/`**: Higher-level agent abstractions
    - `agent_framework.py`: (Currently empty - placeholder for framework code)
    - `artisan_agent.py`: (Currently empty - placeholder for specialized agent)

### Key Architectural Concepts

1. **Stateless vs Stateful LLM Interactions**: Core educational concepts
   - Stateless: Each API call is independent with no conversation memory
   - Stateful: Conversation history is maintained and sent with each request

2. **Function Calling/Tools**: Demonstrates how LLMs can use external functions
   - Weather information retrieval
   - Time queries
   - Mathematical calculations

3. **Token Usage Tracking**: All interactions display token consumption (input/output/total) to teach cost awareness

4. **Azure OpenAI Integration**: Uses the official OpenAI Python SDK with Azure-specific configuration

## Development Patterns

- Environment variables loaded via `python-dotenv`
- Azure OpenAI client configuration centralized in `create_azure_openai_client()`
- Interactive demonstrations use menu-driven selection
- Token usage displayed after each API response for educational purposes
- Error handling with graceful fallbacks in interactive modes

## File Structure Context

- **Root level**: Configuration files (`pyproject.toml`, `.env.example`) and basic entry point
- **Session directories**: Organized learning modules that can be expanded
- **No testing framework**: Currently set up for learning/demonstration, not production code
- **No linting/formatting**: Development environment is minimal and focused on learning