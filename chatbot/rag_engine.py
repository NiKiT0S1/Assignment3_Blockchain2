import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from pymongo import MongoClient
import uuid
import os

# Подключение к MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["constitution_ai"]
collection = db["documents"]

# Модель эмбеддинга
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Сплиттер
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

def process_documents(uploaded_files):
    for file in uploaded_files:
        if file.type == "application/pdf":
            text = extract_text_from_pdf(file)
        elif file.type == "text/plain":
            text = file.read().decode("utf-8")
        else:
            continue

        chunks = text_splitter.split_text(text)
        vectors = embedding_model.encode(chunks).tolist()

        # Сохраняем в MongoDB
        for chunk, vector in zip(chunks, vectors):
            collection.insert_one({
                "_id": str(uuid.uuid4()),
                "text": chunk,
                "embedding": vector
            })

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def retrieve_relevant_chunks(query, top_k=3):
    query_vector = embedding_model.encode([query])[0]

    # Загружаем все документы и считаем косинусную близость
    docs = list(collection.find({}))
    scored = []
    for doc in docs:
        score = cosine_similarity(query_vector, doc["embedding"])
        scored.append((score, doc["text"]))

    scored.sort(reverse=True)
    top_chunks = [text for _, text in scored[:top_k]]
    return top_chunks

def cosine_similarity(a, b):
    import numpy as np
    a, b = np.array(a), np.array(b)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))