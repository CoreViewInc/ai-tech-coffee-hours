import argparse
import os
import uuid
from typing import List, Tuple

from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, PointStruct

from session_1.primitives.shared_utils import embed_texts


load_dotenv()


EMBEDDING_DIM = 1536


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    text = (text or "").strip()
    if not text:
        return []
    chunks = []
    start = 0
    n = len(text)
    while start < n:
        end = min(n, start + chunk_size)
        chunk = text[start:end]
        if end < n:
            split_at = chunk.rfind(" ")
            if split_at > int(chunk_size * 0.6):
                end = start + split_at
                chunk = text[start:end]
        chunks.append(chunk.strip())
        if end >= n:
            break
        start = max(0, end - max(0, overlap))
    return [c for c in chunks if c]


def _embed_texts(texts: List[str]) -> List[List[float]]:
    return embed_texts(texts)


def ensure_collection(client: QdrantClient, name: str, recreate: bool = False):
    if recreate:
        client.recreate_collection(
            collection_name=name,
            vectors_config=VectorParams(size=EMBEDDING_DIM, distance=Distance.COSINE),
        )
        return
    try:
        client.get_collection(name)
    except Exception:
        client.create_collection(
            collection_name=name,
            vectors_config=VectorParams(size=EMBEDDING_DIM, distance=Distance.COSINE),
        )


def read_text_sources(file: str = None, dir: str = None) -> List[Tuple[str, str]]:
    sources = []
    if file:
        with open(file, "r", encoding="utf-8") as f:
            sources.append((file, f.read()))
    if dir:
        for root, _, files in os.walk(dir):
            for fn in files:
                if fn.lower().endswith((".txt", ".md")):
                    path = os.path.join(root, fn)
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            sources.append((path, f.read()))
                    except Exception:
                        pass
    return sources


def upsert_chunks(
    qdrant: QdrantClient,
    collection: str,
    chunks: List[str],
    vectors: List[List[float]],
    source: str,
):
    points = []
    for idx, (text, vec) in enumerate(zip(chunks, vectors)):
        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vec,
                payload={
                    "text": text,
                    "source": source,
                    "chunk_index": idx,
                },
            )
        )
    qdrant.upsert(collection_name=collection, points=points)


def main():
    parser = argparse.ArgumentParser(description="Minimal text importer to Qdrant with embeddings")
    parser.add_argument("--file", type=str, help="Path to a single text file")
    parser.add_argument(
        "--dir",
        type=str,
        default="./session_2/rag/data",
        help="Path to a directory of .txt/.md files (default: ./session_2/rag/data)",
    )
    parser.add_argument("--collection", type=str, default="session2_rag", help="Qdrant collection name")
    parser.add_argument("--chunk-size", type=int, default=500, help="Chunk size in characters")
    parser.add_argument("--overlap", type=int, default=50, help="Character overlap between chunks")
    
    #NOTE: set to false to not recreate collection
    parser.add_argument("--recreate", action="store_true", default=True, help="Drop and recreate collection") 
    args = parser.parse_args()

    qdrant_url = os.getenv("QDRANT_URL", "http://localhost:6333")
    # Embedding deployment is handled by create_azure_embedding_client()

    qdrant = QdrantClient(url=qdrant_url)
    ensure_collection(qdrant, args.collection, recreate=args.recreate)

    # Default to ./data if no --file provided; still honor explicit --dir
    sources = read_text_sources(args.file, args.dir)
    if not sources:
        if args.dir:
            print(f"No sources found under '{args.dir}'. Ensure it contains .txt/.md files.")
        else:
            print("No sources found. Provide --file or --dir with .txt/.md files.")
        return

    total_chunks = 0
    for src_path, content in sources:
        chunks = chunk_text(content, chunk_size=args.chunk_size, overlap=args.overlap)
        print(f"Processing {src_path}: {len(chunks)} chunks")
        if not chunks:
            continue
        vectors = _embed_texts(chunks)
        upsert_chunks(qdrant, args.collection, chunks, vectors, src_path)
        print(f"Ingested {len(chunks)} chunks from {src_path}")
        total_chunks += len(chunks)

    print(f"Done. Total chunks ingested: {total_chunks} into '{args.collection}'.")


if __name__ == "__main__":
    main()
