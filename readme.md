# AI QA Copilot

## Overview

AI QA Copilot is a GenAI-powered Quality Assurance assistant that generates test cases from requirement documents using RAG (Retrieval-Augmented Generation).

The application supports PDF and DOCX uploads and leverages local LLMs via Ollama.

---

## Features

- Upload BRD/SRS documents
- Generate Functional Test Cases
- Generate Negative Test Cases
- Generate Edge Cases
- Semantic Search using Vector Database
- Local LLM Inference using Ollama
- RAG-based Retrieval

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB
- Sentence Transformers
- PyPDF
- Python-Docx

---

## Architecture

Requirement Document
↓
Parser
↓
Chunking
↓
Embeddings
↓
ChromaDB
↓
Retriever
↓
Ollama (Llama3)
↓
Generated Test Cases

---

## Installation

Create virtual environment:

python -m venv venv

Activate:

.\venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## Run

streamlit run streamlitApp.py

---

## Sample Use Case

Input:
User should be able to login using email and password.

Output:
- Functional Test Cases
- Negative Test Cases
- Boundary Tests
- Edge Cases

---

## Future Enhancements

- Jira Integration
- TestRail Integration
- Excel Export
- Multi-Agent Architecture
- Risk-Based Testing

---

## Author

Somil Bajpai
QA Engineer | GenAI Enthusiast