import streamlit as st
import os

from parser import parse_pdf, parse_docx
from rag_pipeline import create_vector_store
from prompts import TESTCASE_PROMPT

from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA



st.set_page_config(
    page_title="AI QA Copilot",
    layout="wide"
)

st.title("AI QA Copilot")
st.subheader("AI-Powered Test Case Generator")


uploaded_file = st.file_uploader(
    "Upload Requirement Document",
    type=["pdf", "docx"]
)

if uploaded_file:

    if not os.path.exists("uploads"):
        os.makedirs("uploads")

    file_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully")

    # Parse File

    if uploaded_file.name.endswith(".pdf"):
        text = parse_pdf(file_path)
    else:
        text = parse_docx(file_path)

    # Create Vector DB

    with st.spinner("Creating vector database..."):

        vectorstore = create_vector_store(text)

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 4}
    )

    # Local Llama Model

    llm = OllamaLLM(
        model="llama3"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    if st.button("Generate Test Cases"):

        with st.spinner("Generating QA scenarios..."):

            query = TESTCASE_PROMPT.format(
                context=text
            )

            result = qa_chain.run(query)
            st.write("QA chain created successfully")
            st.subheader("Generated Test Cases")

            st.write(result)