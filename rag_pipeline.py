from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store(text):

    splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

    chunks=splitter.split_text(text)

    embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vector_store=Chroma.from_texts(
        texts=chunks, 
        embedding=embedding,
        persist_directory="chroma_db")
    
    return vector_store