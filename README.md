# AI Customer Support Automation

An AI-powered customer support system that uses Retrieval-Augmented Generation (RAG) to resolve queries automatically — delivering accurate, context-aware responses without human intervention.

---

## 🧠 How It Works

```
Customer Query (via API)
        ↓
Ollama (bge-m3) generates semantic embedding
        ↓
FAISS retrieves most relevant support documents
        ↓
Gemini generates a grounded, accurate response
        ↓
Response returned via FastAPI
```

---

## ✨ Features

- **Automated query resolution** using AI agents — no human needed for common queries
- **Semantic search with FAISS** for fast, relevant document retrieval
- **Hybrid architecture** — Ollama embeddings + Gemini generation for best-in-class accuracy
- **Real-time API** — query handling and response generation via FastAPI
- **Grounded responses** — answers pulled from actual support docs, not hallucinated
- **Logging & experimentation framework** for performance monitoring and optimization

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **API Framework** | FastAPI |
| **LLM** | Gemini |
| **Embeddings** | Ollama (bge-m3) |
| **Vector Store** | FAISS |
| **Language** | Python |

---

## ⚙️ Setup & Installation

```bash
# 1. Clone the repository
git clone https://github.com/prathamparmar1/AI-Customer-Support.git
cd AI-Customer-Support

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Pull Ollama model
ollama pull bge-m3

# 5. Set up environment variables
cp .env.example .env
```

---

## 🔑 Environment Variables

```env
GEMINI_API_KEY=your_gemini_api_key
OLLAMA_BASE_URL=http://localhost:11434
```

---

## 🚀 Usage

```bash
# Start the FastAPI server
uvicorn main:app --reload

# API is now live at http://localhost:8000
# POST /query — submit a customer support question
```

**Example request:**
```json
POST /query
{
  "question": "How do I reset my password?"
}
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/query` | Submit a support query |
| GET | `/health` | Health check |
| GET | `/logs` | View query logs |

---

## 📬 Contact

**Pratham Parmar** — [prathamparmar203@gmail.com](mailto:prathamparmar203@gmail.com) · [Portfolio](https://prathamparmar-portfolio.vercel.app/) · [LinkedIn](https://linkedin.com/in/prathamparmar1)
