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