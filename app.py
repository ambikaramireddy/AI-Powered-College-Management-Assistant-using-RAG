import os
import streamlit as st

from src.router import classify_query
from src.pdf_rag import get_retriever
from src.llm_client import hf_chat
from src.prompts import *

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="College Management Chatbot",
    page_icon="🎓",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.stChatMessage {
    padding: 10px;
    border-radius: 10px;
}

h1 {
    color: #003366;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🎓 College Management Assistant")
st.caption("Ask about admissions, fees, departments, placements, hostel, exams, and more.")

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_name" not in st.session_state:
    st.session_state.user_name = None

# ---------------------------------------------------
# LOAD RETRIEVER
# ---------------------------------------------------

if "retriever" not in st.session_state:

    with st.spinner("Loading college knowledge base..."):

        try:
            st.session_state.retriever = get_retriever("data")
            st.success("Knowledge Base Loaded Successfully ✅")

        except Exception as e:
            st.error(f"Error loading PDFs: {e}")
            st.session_state.retriever = None

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.header("⚙ Configuration")

    st.success("System Ready")

    st.write("### Chat Model")
    st.code(
        os.getenv(
            "HF_CHAT_MODEL",
            "meta-llama/Llama-3.1-8B-Instruct"
        )
    )

    st.write("### Embedding Model")
    st.code(
        os.getenv(
            "HF_EMBEDDING_MODEL",
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    st.write("### Features")

    st.markdown("""
    - PDF-based RAG
    - FAISS Vector Search
    - Hugging Face LLM
    - Smart Query Routing
    - College Information Retrieval
    """)

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        if "user_name" in st.session_state:
            st.session_state.user_name = None

        st.rerun()

# ---------------------------------------------------
# DISPLAY CHAT HISTORY
# ---------------------------------------------------

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ---------------------------------------------------
# USER INPUT
# ---------------------------------------------------

user_input = st.chat_input(
    "Ask about admissions, fees, exams, placements..."
)

# ---------------------------------------------------
# CHATBOT LOGIC
# ---------------------------------------------------

def generate_response(user_input, history):

    text = user_input.lower().strip()

    # Greetings
    greetings = ["hi", "hello", "hey"]

    if text in greetings:
        return "Hello! How can I help you today?", []

    # Bot Name
    if "your name" in text:
        return "I am Alex, your college assistant.", []

    # Store User Name
    if "my name is" in text:

        name = user_input.split("is")[-1].strip().title()

        st.session_state.user_name = name

        return f"Nice to meet you, {name}.", []

    # Recall Name
    if "my name" in text:

        if st.session_state.user_name:
            return (
                f"Your name is {st.session_state.user_name}.",
                []
            )

        return ("I don't know your name yet.", [])

    # Weather
    if "weather" in text:
        return (
            "I currently cannot provide live weather updates.",
            []
        )

    # Features
    if "what can you do" in text or "what information" in text:

        return (
            "I can provide information about admissions, fees, departments, placements, hostel facilities, academic schedules, exams, and other college-related details.",
            []
        )

    # Route Query
    route = classify_query(user_input)

    # GENERAL
    if route == "GENERAL":

        answer = hf_chat(
            general_prompt(user_input, history)
        )

        return answer, []

    # RAG SEARCH
    retriever = st.session_state.retriever

    if retriever is None:
        return (
            "Knowledge base not loaded properly.",
            []
        )

    docs = retriever.retrieve(
        user_input,
        top_k=5
    )

    context = "\n\n".join([
        f"[Source: {d['source']}, page {d['page']}]\n{d['text']}"
        for d in docs
    ])

    answer = hf_chat(
        college_prompt(
            user_input,
            history,
            context
        )
    )

    return answer, docs

# ---------------------------------------------------
# PROCESS INPUT
# ---------------------------------------------------

if user_input:

    # USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # HISTORY
    history = "\n".join([
        f'{m["role"]}: {m["content"]}'
        for m in st.session_state.messages[-8:]
    ])

    # ASSISTANT RESPONSE
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, sources = generate_response(
                user_input,
                history
            )

            st.markdown(answer)

            # SHOW SOURCES
            if sources:

                with st.expander("📚 Sources Used"):

                    for i, doc in enumerate(sources, start=1):

                        st.markdown(
                            f"### {i}. {doc['source']} — Page {doc['page']}"
                        )

                        st.write(
                            doc["text"][:500] +
                            ("..." if len(doc["text"]) > 500 else "")
                        )

    # SAVE RESPONSE
    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })