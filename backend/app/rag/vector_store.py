import chromadb
import uuid

from langchain_text_splitters import RecursiveCharacterTextSplitter

from sentence_transformers import SentenceTransformer


# Chroma database client
client = chromadb.PersistentClient(
    path="chroma_db"
)

# Collection
collection = client.get_or_create_collection(
    name="blood_reports"
)

# Embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def store_document(text: str):

    """
    Split text into chunks,
    create embeddings,
    save into ChromaDB
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_text(text)

    for index, chunk in enumerate(chunks):

        embedding = embedding_model.encode(
            chunk
        ).tolist()

        collection.add(
            ids=[str(uuid.uuid4())],
            documents=[chunk],
            embeddings=[embedding]
        )

    return len(chunks)