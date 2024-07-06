# RAG Model using Langchain

This project demonstrates a simple implementation of a Retrieval-Augmented Generation (RAG) system using free Hugging Face models. It includes functionalities for creating a database of text documents, querying the database, and comparing embeddings.

## Project Structure

rag_project/
│
├── .env
├── requirements.txt
├── create_database.py
├── query_data.py
├── compare_embeddings.py
│
├── data/
│ └── books/
│ ├── book1/
│ │ ├── chapter1.md
│ │ └── chapter2.md
│ └── book2/
│ ├── chapter1.txt
│ └── chapter2.txt
│
└── chroma/
└── (generated database files)

