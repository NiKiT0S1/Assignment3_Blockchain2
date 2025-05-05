import subprocess

# Можно заменить на свою модель, если требуется
OLLAMA_MODEL = "llama3"

def generate_answer(question, context_chunks):
    context = "\n---\n".join(context_chunks)
    # prompt = f"""You are a helpful assistant. Use the context below to answer the question.
    prompt = f"""You are a helpful multilingual assistant. Use the context below to answer the question in the **same language** the question is asked in.

Context:
{context}

Question: {question}
Answer:"""

    try:
        # Вызов модели через ollama CLI
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )
        response = result.stdout.decode("utf-8").strip()
        return response

    except subprocess.TimeoutExpired:
        return "⚠️ Model timed out."
    except Exception as e:
        return f"⚠️ Error: {e}"