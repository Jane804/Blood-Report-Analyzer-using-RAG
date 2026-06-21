from app.rag.vector_store import (
    collection,
    embedding_model
)


def retrieve_context(
    question: str,
    top_k: int = 3
):
    """
    Retrieve most relevant chunks
    from ChromaDB
    """

    query_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results["documents"][0]

    context = "\n".join(documents)

    return context