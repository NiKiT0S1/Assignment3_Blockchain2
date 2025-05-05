from pymongo import MongoClient
from datetime import datetime
import os

# Подключение к MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
client = MongoClient(MONGO_URI)
db = client["constitution_ai"]
qa_collection = db["chat_history"]

def save_qa_to_db(question, answer):
    qa_collection.insert_one({
        "question": question,
        "answer": answer,
        "timestamp": datetime.utcnow()
    })

def get_chat_history(limit=10):
    return list(qa_collection.find().sort("timestamp", -1).limit(limit))

def clear_database():
    from pymongo import MongoClient
    import os
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = MongoClient(MONGO_URI)
    db = client["constitution_ai"]
    db["documents"].delete_many({})  # удаляет все документы
    db["chat_history"].delete_many({}) # удаляет всю историю