<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RAG Project</title>
</head>
<body>
    <h1>RAG Project</h1>
    <p>This project demonstrates a simple implementation of a Retrieval-Augmented Generation (RAG) system using free Hugging Face models. It includes functionalities for creating a database of text documents, querying the database, and comparing embeddings.</p>
    
    <h2>Project Structure</h2>
    <pre>
rag_project/
│
├── .env
├── requirements.txt
├── create_database.py
├── query_data.py
├── compare_embeddings.py
│
├── data/
│   └── books/
│       ├── book1/
│       │   ├── chapter1.md
│       │   └── chapter2.md
│       └── book2/
│           ├── chapter1.txt
│           └── chapter2.txt
│
└── chroma/
    └── (generated database files)
    </pre>
    
    <h2>Requirements</h2>
    <ul>
        <li>Python 3.8+</li>
        <li>pip</li>
    </ul>
    
    <h2>Setup</h2>
    <ol>
        <li><strong>Clone the repository:</strong>
            <pre><code>git clone https://github.com/your-username/rag_project.git
cd rag_project</code></pre>
        </li>
        <li><strong>Create and activate a virtual environment:</strong>
            <p>On Windows:</p>
            <pre><code>python -m venv venv
venv\Scripts\activate</code></pre>
            <p>On macOS/Linux:</p>
            <pre><code>python3 -m venv venv
source venv/bin/activate</code></pre>
        </li>
        <li><strong>Install the requirements:</strong>
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li><strong>Create an empty .env file:</strong>
            <pre><code>touch .env</code></pre>
        </li>
    </ol>
    
    <h2>Usage</h2>
    <ol>
        <li><strong>Create the database:</strong>
            <pre><code>python create_database.py</code></pre>
        </li>
        <li><strong>Query the database:</strong>
            <pre><code>python query_data.py "Your question here"</code></pre>
        </li>
        <li><strong>Compare embeddings (optional):</strong>
            <pre><code>python compare_embeddings.py</code></pre>
        </li>
    </ol>
    
    <h2>Explanation of Scripts</h2>
    <ul>
        <li><strong>create_database.py:</strong> Loads documents, splits them into chunks, generates embeddings, and saves them to a Chroma vector store.</li>
        <li><strong>query_data.py:</strong> Queries the Chroma database using similarity search and generates a response using a text generation model.</li>
        <li><strong>compare_embeddings.py:</strong> Demonstrates how to generate embeddings for words and compare their similarity.</li>
    </ul>
    
    <h2>Directory Structure</h2>
    <p><strong>data/books/:</strong> Place your books in Markdown (.md) or text (.txt) format here. Each book should be in its own subdirectory.</p>
    <p><strong>chroma/:</strong> This directory will be generated to store the Chroma database files.</p>
    
    <h2>Sample Data Structure</h2>
    <pre>
data/
└── books/
    ├── book1/
    │   ├── chapter1.md
    │   └── chapter2.md
    └── book2/
        ├── chapter1.txt
        └── chapter2.txt
    </pre>
    
    <h2>.gitignore</h2>
    <pre><code>
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
*.pdb

# Virtual Environment
venv/

# Environment variables
.env

# Chroma database files
chroma/
    </code></pre>
    
    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
    
    <h2>Contributing</h2>
    <p>Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.</p>
    
    <h2>Acknowledgements</h2>
    <ul>
        <li><a href="https://huggingface.co/">Hugging Face</a></li>
        <li><a href="https://github.com/hwchase17/langchain">LangChain</a></li>
        <li><a href="https://github.com/chroma-core/chroma">Chroma</a></li>
        <li><a href="https://github.com/Unstructured-IO/unstructured">Unstructured</a></li>
    </ul>
    
    <h2>Commands to Push the Project to GitHub</h2>
    <ol>
        <li><strong>Initialize a local git repository:</strong>
            <pre><code>git init</code></pre>
        </li>
        <li><strong>Add all files to the repository:</strong>
            <pre><code>git add .</code></pre>
        </li>
        <li><strong>Commit the files:</strong>
            <pre><code>git commit -m "Initial commit"</code></pre>
        </li>
        <li><strong>Create a new repository on GitHub.</strong></li>
        <li><strong>Add the remote repository URL:</strong>
            <pre><code>git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git</code></pre>
        </li>
        <li><strong>Push the changes to GitHub:</strong>
            <pre><code>git push -u origin master</code></pre>
            <p>If your default branch is <code>main</code> instead of <code>master</code>:</p>
            <pre><code>git push -u origin main</code></pre>
        </li>
    </ol>
</body>
</html>
