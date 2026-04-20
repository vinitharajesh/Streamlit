import streamlit as st
from langchain_community.document_loaders import TextLoader, PyPDFLoader, Docx2txtLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

# -------------------------
# UI Title
# -------------------------
st.title("🧠 Local AI Document Assistant")

# -------------------------
# File Upload
# -------------------------
uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])

if uploaded_file is not None:

    # Save file temporarily
    with open("temp_file", "wb") as f:
        f.write(uploaded_file.read())

    file_path = "Sreamlite/Nature.txt"

    # -------------------------
    # Load file
    # -------------------------
    if uploaded_file.name.endswith(".txt"):
        loader = TextLoader(file_path)

    elif uploaded_file.name.endswith(".pdf"):
        loader = PyPDFLoader(file_path)

    elif uploaded_file.name.endswith(".docx"):
        loader = Docx2txtLoader(file_path)

    else:
        st.error("Unsupported file type")
        st.stop()

    documents = loader.load()

    # -------------------------
    # Split text
    # -------------------------
    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    docs = splitter.split_documents(documents)

    # -------------------------
    # Embeddings
    # -------------------------
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # -------------------------
    # Vector DB
    # -------------------------
    db = FAISS.from_documents(docs, embeddings)

    st.success("✅ Document processed! Ask questions below 👇")

    # -------------------------
    # Load LLM
    # -------------------------
    llm = Ollama(model="tinyllama")  # or llama3, mistral

    # -------------------------
    # Chat UI
    # -------------------------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input
    query = st.chat_input("Ask a question about your document")

    if query:
        st.chat_message("user").write(query)
        st.session_state.messages.append({"role": "user", "content": query})

        # -------------------------
        # RAG
        # -------------------------
        retrieved_docs = db.similarity_search(query, k=3)
        context = " ".join([doc.page_content for doc in retrieved_docs])

        # -------------------------
        # Prompt
        # -------------------------
        prompt = f"""
        You are an AI assistant.

        Answer ONLY using the context below.
        If the answer is not in the context, say "I don't know".

        Context:
        {context}

        Question:
        {query}

        Answer:
        """

        # -------------------------
        # Generate response
        # -------------------------
        response = llm.invoke(prompt)

        st.chat_message("assistant").write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})