# RAG Project

This project demonstrates a simple implementation of a Retrieval-Augmented Generation (RAG) system using free Hugging Face models. It includes functionalities for creating a database of text documents, querying the database, and comparing embeddings.

## Project Structure
<ul>
  <li>.env</li>
  <li>requirements.txt</li>
  <li>create_database.py</li>
  <li>query_data.py</li>
  <li>compare_embeddings.py</li>
  <li>data/
    <ul>
      <li>books/
        <ul>
          <li>book1/
            <ul>
              <li>chapter1.md</li>
              <li>chapter2.md</li>
            </ul>
          </li>
          <li>book2/
            <ul>
              <li>chapter1.txt</li>
              <li>chapter2.txt</li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>chroma/
    <ul>
      <li>(generated database files)</li>
    </ul>
  </li>
</ul>

## Requirements
<ul>
  <li>Python 3.8+</li>
  <li>pip</li>
</ul>

## Setup
1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/rag_project.git
    cd rag_project
    ```
2. **Create and activate a virtual environment:**
    - On Windows:
        ```sh
        python -m venv venv
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```
3. **Install the requirements:**
    ```sh
    pip install -r requirements.txt
    ```
4. **Create an empty .env file:**
    ```sh
    touch .env
    ```

## Usage
1. **Create the database:**
    ```sh
    python create_database.py
    ```
2. **Query the database:**
    ```sh
    python query_data.py "Your question here"
    ```
3. **Compare embeddings (optional):**
    ```sh
    python compare_embeddings.py
    ```

## Explanation of Scripts
<ul>
  <li><strong>create_database.py:</strong> Loads documents, splits them into chunks, generates embeddings, and saves them to a Chroma vector store.</li>
  <li><strong>query_data.py:</strong> Queries the Chroma database using similarity search and generates a response using a text generation model.</li>
  <li><strong>compare_embeddings.py:</strong> Demonstrates how to generate embeddings for words and compare their similarity.</li>
</ul>

## Directory Structure
<p><strong>data/books/:</strong> Place your books in Markdown (.md) or text (.txt) format here. Each book should be in its own subdirectory.</p>
<p><strong>chroma/:</strong> This directory will be generated to store the Chroma database files.</p>


## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements
<ul>
  <li><a href="https://huggingface.co/">Hugging Face</a></li>
  <li><a href="https://github.com/hwchase17/langchain">LangChain</a></li>
  <li><a href="https://github.com/chroma-core/chroma">Chroma</a></li>
  <li><a href="https://github.com/Unstructured-IO/unstructured">Unstructured</a></li>
</ul>

## Sample Data Structure
```sh
data/
└── books/
    ├── book1/
    │   ├── chapter1.md
    │   └── chapter2.md
    └── book2/
        ├── chapter1.txt
        └── chapter2.txt
