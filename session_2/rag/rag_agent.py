import os
import json
from typing import List

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

from session_1.primitives.shared_utils import create_azure_openai_client, embed_query


load_dotenv()


def _require_env(key: str, hint: str) -> str:
    val = os.getenv(key)
    if not val:
        raise RuntimeError(
            f"Missing environment variable {key}. {hint}"
        )
    return val


def _embed_query(text: str) -> List[float]:
    embedding_deployment = _require_env(
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME",
        "Set it to your Azure embedding deployment name (not the base model id), e.g. 'emb-small'.",
    )
    return embed_query(text, model=embedding_deployment)


def retrieve_passages(query: str, top_k: int = 4, collection: str = "session2_rag") -> str:
    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    qdrant_api_key = os.getenv("QDRANT_API_KEY")
    vec = _embed_query(query)
    client = QdrantClient(url=qdrant_url, api_key=qdrant_api_key)

    search_result = client.search(
        collection_name=collection,
        query_vector=vec,
        limit=max(1, min(top_k, 10)),
        score_threshold=0.4,
    )

    items = []
    for p in search_result:
        items.append(
            {
                "text": p.payload.get("text"),
                "source": p.payload.get("source"),
                "score": p.score,
            }
        )
    
    return json.dumps({"results": items})


tools = [
    {
        "type": "function",
        "function": {
            "name": "retrieve_passages",
            "description": "Retrieve top-k relevant chunks from the Qdrant vector store",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Natural language query. Improve it to get better results."},
                    "top_k": {"type": "number", "description": "Number of chunks to retrieve (1-10)", "default": 4},
                    "collection": {"type": "string", "description": "Qdrant collection name", "default": "session2_rag"},
                },
                "required": ["query"],
            },
        },
    }
]


def demonstrate_rag_agent():
    print("\n" + "=" * 60)
    print("RAG AGENT (Retriever as Tool)")
    print("Ask questions about your imported texts.")
    print("Type 'quit' to exit")
    print("=" * 60 + "\n")

    client = create_azure_openai_client()
    deployment_name = _require_env(
        "AZURE_DEPLOYMENT_NAME",
        "Set it to your Azure chat/completions deployment name (not the base model id).",
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful assistant that answers using a retriever tool when helpful."
                " When tool results are available, cite relevant snippets concisely."
            ),
        }
    ]

    while True:
        user_input = input("\nYou: ")
        if user_input.strip().lower() == "quit":
            print("Goodbye!")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model=deployment_name,
                messages=messages,
                tools=tools,
                tool_choice="auto",
                temperature=0.3,
            )

            first = response.choices[0].message
            tool_calls = first.tool_calls

            if tool_calls:
                messages.append(first)
                for call in tool_calls:
                    fn = call.function.name
                    args = json.loads(call.function.arguments or "{}")
                    if fn == "retrieve_passages":
                        print("🔎 Retrieving relevant passages...")
                        result = retrieve_passages(**args)
                        messages.append(
                            {
                                "tool_call_id": call.id,
                                "role": "tool",
                                "name": fn,
                                "content": result,
                            }
                        )

                follow_up = client.chat.completions.create(
                    model=deployment_name,
                    messages=messages,
                    temperature=0.3,
                )
                final = follow_up.choices[0].message.content
                usage = follow_up.usage
                print(f"\nAssistant: {final}")
                print(
                    f"📊 Tokens - Input: {usage.prompt_tokens}, Output: {usage.completion_tokens}, Total: {usage.total_tokens}"
                )
                messages.append({"role": "assistant", "content": final})
            else:
                msg = first.content
                usage = response.usage
                print(f"Assistant: {msg}")
                print(
                    f"📊 Tokens - Input: {usage.prompt_tokens}, Output: {usage.completion_tokens}, Total: {usage.total_tokens}"
                )
                messages.append({"role": "assistant", "content": msg})

        except Exception as e:
            print(f"Error: {e}")
            break

    print("\n✅ RAG agent demo complete.")


if __name__ == "__main__":
    demonstrate_rag_agent()
