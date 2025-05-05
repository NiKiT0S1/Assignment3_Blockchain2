# 🤖 AI Constitution Assistant 🤖

**AI Constitution Assistant** is a Streamlit application that leverages LangChain, Ollama, and MongoDB technologies to answer questions related to the Constitution of the Republic of Kazakhstan, as well as your uploaded PDF and TXT documents.

## 🧠 Features
- 📜 Answers questions about the Constitution of Kazakhstan
- 📂 Allows uploading your own documents (PDF, TXT)
- 🤖 Uses a local LLM model (default: `llama3` via [Ollama](https://ollama.com/))
- 💬 Saves the history of questions and answers in MongoDB
- 🔎 Extracts relevant text fragments through semantic search
- 🌐 Supports English and Russian languages

## 🛠️ Technology Stack
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [SentenceTransformers](https://www.sbert.net/)
- [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- [MongoDB](https://www.mongodb.com/)
- [Ollama](https://ollama.com/) + LLM model (`llama3` by default)

## 🚀 Project Setup
### 1. Install dependencies
```bash
pip install -r requirements.txt
```

<details>
<summary>Example requirements.txt</summary>

```
streamlit
pymongo
sentence-transformers
pymupdf
langchain
```
</details>

### 2. Install and run Ollama
```bash
# Install Ollama
ollama run llama3
```

### 3. Run the Streamlit application
```bash
streamlit run main.py
```

### 4. (Optional) Specify Mongo URI
By default, it uses:
```
mongodb://localhost:27017
```

You can override it with an environment variable:
```bash
export MONGO_URI="mongodb://your_mongodb_host:27017"
```

## 📁 Project Structure
```
📦 ai-constitution-assistant/
├── main.py                # Streamlit interface
├── db.py                  # MongoDB operations
├── rag_engine.py          # RAG (Embedding + Search)
└── chat_handler.py        # LLM response generation
```

## 💡 Example Questions
- 🇬🇧 What is the role of the President according to the Constitution?
- 🇷🇺 Какие права имеет гражданин Казахстана согласно Конституции?

## 📌 Notes
- Documents are uploaded to MongoDB as vector representations.
- After uploading, new questions are processed in the context of these documents.
- The "Clear document database" button removes all vectors but not the chat history.

## 🧹 Database Cleanup
To remove all documents from the database, click the "🗑️ Clear document database" button in the interface.

## 🔒 Security
- The application runs locally.
- All data is stored in your MongoDB.
- The Ollama model runs locally, without sending data to the internet.

## LICENCE
The MIT License (MIT)

Copyright (c) 2016-2025 Zeppelin Group Ltd

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

