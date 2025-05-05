import streamlit as st
from rag_engine import process_documents, retrieve_relevant_chunks
from chat_handler import generate_answer
from db import save_qa_to_db
import os

from db import clear_database

st.set_page_config(page_title="AI Constitution Assistant", layout="wide")

# st.title("🇰🇿 AI Assistant — Constitution of Kazakhstan")
st.title("""
 🤖 **AI Constitution Assistant** 🤖
### _Your legal helper powered by AI_ 🤝
""")
st.write("Ask any question about the Constitution or your uploaded documents.")

# Инициализация сессии
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Форма загрузки файлов
uploaded_files = st.file_uploader("Upload document(s)", type=["pdf", "txt"], accept_multiple_files=True)
if uploaded_files:
    docs_loaded = process_documents(uploaded_files)
    st.success(f"{len(uploaded_files)} document(s) processed and indexed.")


if "clear_triggered" not in st.session_state:
    st.session_state.clear_triggered = False


if st.button("🗑️ Очистить базу документов"):
    clear_database()
    st.success("База документов очищена.")
    # st.stop()
    st.session_state.clear_triggered = True


# Ввод вопроса пользователем
user_query = st.text_input("Enter your question:")

if user_query and not st.session_state.clear_triggered:
    # Поиск релевантного контекста
    context_chunks = retrieve_relevant_chunks(user_query)

    # Генерация ответа через LLM
    answer = generate_answer(user_query, context_chunks)

    # Отображение ответа
    st.markdown(f"**Answer:** {answer}")

    # Сохранение истории в MongoDB
    save_qa_to_db(user_query, answer)

    # Добавление в сессию
    st.session_state.chat_history.append((user_query, answer))


if st.session_state.clear_triggered:
    st.session_state.clear_triggered = False


# История чата
if st.session_state.chat_history:
    st.subheader("Chat History")
    for q, a in st.session_state.chat_history[::-1]:
        st.markdown(f"**Q:** {q}")
        st.markdown(f"**A:** {a}")
        st.markdown("---")