import os
import shutil
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader, UnstructuredMarkdownLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

CHROMA_PATH = "chroma"
DATA_PATH = "data/books"

def main():
    generate_data_store()

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    md_loader = DirectoryLoader(DATA_PATH, glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    txt_loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", loader_cls=TextLoader)
    
    md_docs = md_loader.load()
    txt_docs = txt_loader.load()
    
    documents = md_docs + txt_docs
    
    for doc in documents:
        doc.metadata["book"] = os.path.basename(os.path.dirname(doc.metadata["source"]))
    
    print(f"Loaded {len(documents)} documents")
    return documents

def split_text(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks")
    return chunks

def save_to_chroma(chunks):
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(
        chunks, embedding_function, persist_directory=CHROMA_PATH
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_PATH}")

if __name__ == "__main__":
    main()