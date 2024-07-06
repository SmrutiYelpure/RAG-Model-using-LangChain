from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def main():
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Get embedding for a word
    vector = embedding_function.embed_query("apple")
    print(f"Vector for 'apple': {vector[:5]}...")  # Showing first 5 elements
    print(f"Vector length: {len(vector)}")

    # Compare vector of two words
    words = ("apple", "iphone")
    vectors = [embedding_function.embed_query(word) for word in words]
    similarity = cosine_similarity([vectors[0]], [vectors[1]])[0][0]
    print(f"Comparing ({words[0]}, {words[1]}): Cosine similarity = {similarity}")

if __name__ == "__main__":
    main()