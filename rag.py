import faiss
import numpy as np
import requests

documents = []
index = None

OLLAMA_URL = "http://localhost:11434/api/embed"
MODEL_NAME = "bge-m3"

def load_data():
    global documents
    with open("data/knowledge.txt", "r") as f:
        documents = [line.strip() for line in f.readlines() if line.strip()]

def get_embeddings(text_list):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "input": text_list
    })

    if response.status_code != 200:
        raise Exception(f"Ollama error: {response.text}")

    return response.json()["embeddings"]

def build_index():
    global index

    embeddings = get_embeddings(documents)
    embeddings = np.array(embeddings).astype("float32")

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

def retrieve(query, k=2):
    query_embedding = get_embeddings([query])[0]
    query_embedding = np.array([query_embedding]).astype("float32")

    distances, indices = index.search(query_embedding, k)

    return [documents[i] for i in indices[0]]