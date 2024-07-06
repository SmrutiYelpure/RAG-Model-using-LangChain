import argparse
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import pipeline

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Question: {question}
Answer:"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text

    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        print(f"Unable to find matching results.")
        return

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["context", "question"])
    
    llm = HuggingFacePipeline.from_model_id(
        model_id="google/flan-t5-base",
        task="text2text-generation",
        model_kwargs={"temperature": 0.5, "max_length": 512},
    )
    
    llm_chain = LLMChain(prompt=prompt_template, llm=llm)

    response = llm_chain.run(context=context_text, question=query_text)

    sources = [f"{doc.metadata.get('book', 'Unknown')}: {doc.metadata.get('source', None)}" for doc, _score in results]
    formatted_response = f"Response: {response}\nSources: {sources}"
    print(formatted_response)

if __name__ == "__main__":
    main()