# 🎓 CampusGPT

### AI-Powered College Management Assistant using Retrieval-Augmented Generation (RAG)

<p align="center">
  <b>Ask questions. Retrieve relevant college information. Get grounded AI answers.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit">
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/LangChain-RAG-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/FAISS-VectorDB-yellow?style=for-the-badge">
  <img src="https://img.shields.io/badge/HuggingFace-LLM-yellow?style=for-the-badge&logo=huggingface">
</p>

---

## 📌 Overview

**CampusGPT** is an AI-powered college management assistant that uses **Retrieval-Augmented Generation (RAG)** to answer student queries using information stored in institutional documents.

Instead of manually searching through multiple college PDFs, students can ask questions in natural language such as:

> **"What are the hostel facilities?"**

> **"What is the admission process?"**

> **"Tell me about the fee structure."**

> **"What placement opportunities are available?"**

The system retrieves the most relevant information from the college knowledge base and provides a contextual response using a Large Language Model.

### 💡 Core Idea

**College Documents → Text Extraction → Chunking → Embeddings → FAISS → Semantic Retrieval → LLM → Final Answer**

---

## 🚀 Live Demo

Try the deployed application:

### 🔗 [CampusGPT Live Application](https://ai-powered-college-management-assistant-using-rag-pgkgzd2ahtxo.streamlit.app/)

The application allows users to:

* 💬 Ask college-related questions
* 📄 Retrieve information from PDF documents
* 🔎 Perform semantic document search
* 🤖 Generate contextual AI responses
* ⚡ Get information quickly through a conversational interface

---

## 🎯 Problem Statement

College information is often distributed across multiple documents, notices, brochures, websites, and PDFs.

Students may need to manually search for information related to:

* Admissions
* Courses
* Fee structure
* Hostel facilities
* Placements
* Academic information
* Campus facilities
* College policies

Traditional document-search methods can be time-consuming and difficult for users who do not know exactly where the required information is located.

### Proposed Solution

CampusGPT provides a conversational interface where students can simply ask a question.

The system:

1. Understands the user's query.
2. Searches the college knowledge base using semantic similarity.
3. Retrieves the most relevant document chunks.
4. Passes the retrieved context to an LLM.
5. Generates a grounded response based on the retrieved information.

---

# ✨ Key Features

| Feature                   | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| 💬 Conversational Chatbot | Ask questions using natural language                     |
| 📄 PDF Knowledge Base     | Uses institutional PDF documents as the knowledge source |
| 🔎 Semantic Search        | Retrieves relevant information based on meaning          |
| 🧠 RAG Pipeline           | Combines retrieval with LLM generation                   |
| 🗃️ FAISS Vector Database | Enables fast similarity search                           |
| 🤖 Hugging Face LLM       | Generates contextual responses                           |
| 🧩 Query Routing          | Classifies queries before retrieval                      |
| 🌐 Streamlit UI           | Simple and interactive user interface                    |
| ⚡ FastAPI Backend         | Provides API-based backend services                      |
| 🔍 Monitoring             | LangSmith can be used for tracing and monitoring         |

---

# 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                 ┌───────────────────┐
                 │ Streamlit UI      │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Query Router      │
                 │ / Classification  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Query Embedding   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ FAISS Retriever   │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Relevant PDF      │
                 │ Chunks            │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Context + Prompt  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Hugging Face LLM  │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │ Final Response    │
                 └───────────────────┘
```

---

# 🔄 RAG Pipeline

CampusGPT follows a two-stage architecture:

## 1. 📚 Knowledge Base Creation

College PDF documents are processed before users start asking questions.

```text
PDF Documents
      │
      ▼
Text Extraction
      │
      ▼
Document Cleaning
      │
      ▼
Text Chunking
      │
      ▼
Embedding Generation
      │
      ▼
FAISS Vector Index
```

### Step-by-step

**PDF Extraction**

Text is extracted from college PDF documents using PDF processing libraries.

**Text Chunking**

Large documents are divided into smaller chunks so that relevant sections can be retrieved efficiently.

**Embedding Generation**

Each chunk is converted into a numerical vector using an embedding model.

**Vector Storage**

The embeddings are stored in a FAISS index for similarity-based retrieval.

---

## 2. 🤖 Question Answering

When a student asks a question:

```text
User Question
      │
      ▼
Query Processing
      │
      ▼
Query Embedding
      │
      ▼
FAISS Similarity Search
      │
      ▼
Top Relevant Chunks
      │
      ▼
Prompt + Retrieved Context
      │
      ▼
Large Language Model
      │
      ▼
Grounded Answer
```

This approach helps the LLM answer questions using the available institutional information instead of relying only on its pretrained knowledge.

---

# 🛠️ Technology Stack

| Technology                | Role in Project                        |
| ------------------------- | -------------------------------------- |
| **Python**                | Core application development           |
| **Streamlit**             | Interactive frontend                   |
| **FastAPI**               | Backend REST API                       |
| **LangChain**             | RAG workflow and LLM orchestration     |
| **FAISS**                 | Vector similarity search               |
| **Hugging Face**          | Embedding and LLM integration          |
| **PyPDF**                 | PDF text extraction                    |
| **NumPy**                 | Numerical/vector operations            |
| **LangSmith**             | LLM application monitoring and tracing |
| **Python Text Splitters** | Document chunking                      |

---

# 📂 Project Structure

```text
CampusGPT/
│
├── app.py                    # Streamlit frontend
├── api.py                    # FastAPI backend
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── README.md
│
├── data/
│   └── college.pdf           # College knowledge base
│
└── src/
    ├── router.py             # Query classification/routing
    ├── prompts.py            # Prompt templates
    ├── pdf_rag.py            # PDF processing and RAG
    ├── hf_embeddings.py      # Embedding model integration
    ├── llm_client.py         # LLM integration
    └── ...
```

---

# 📘 Module Responsibilities

### `app.py`

Provides the Streamlit-based chatbot interface through which users interact with CampusGPT.

### `api.py`

Implements the FastAPI backend and exposes endpoints for health checks and query processing.

### `router.py`

Classifies incoming questions and determines the appropriate processing route.

### `pdf_rag.py`

Handles PDF processing, document retrieval, and the RAG workflow.

### `hf_embeddings.py`

Generates vector embeddings for documents and user queries.

### `llm_client.py`

Handles communication with the configured Hugging Face language model.

### `prompts.py`

Contains prompt templates used to guide the LLM toward contextual and relevant responses.

---

# 💬 Example Interaction

### 👤 User

```text
Tell me about hostel facilities.
```

### 🔎 Retrieval

CampusGPT searches the FAISS vector index and retrieves the most relevant hostel-related document chunks.

### 🤖 AI Response

```text
The college provides separate hostel facilities for boys and girls.
The hostel includes accommodation, food facilities, Wi-Fi connectivity,
security, and other student amenities.

For detailed hostel fees and availability, please refer to the
official college information provided in the knowledge base.
```

The response is generated using the retrieved document context.

---

# 🔌 API Documentation

CampusGPT also provides a FastAPI backend.

## Health Check

```http
GET /health
```

### Example Response

```json
{
  "status": "healthy"
}
```

---

## Query Endpoint

```http
POST /query
```

### Request

```json
{
  "question": "Tell me about hostel facilities"
}
```

### Response

```json
{
  "route": "COLLEGE_INFO",
  "question": "Tell me about hostel facilities",
  "answer": "The college provides hostel facilities...",
  "sources": [
    {
      "source": "Hostel_Info.pdf",
      "page": 2,
      "text": "The college provides separate hostel facilities..."
    }
  ]
}
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/CampusGPT.git
cd CampusGPT
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root:

```env
HF_TOKEN=your_huggingface_token

HF_PROVIDER=hf-inference

HF_CHAT_MODEL=meta-llama/Llama-3.1-8B-Instruct

HF_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

> ⚠️ Never commit your actual API keys or tokens to GitHub.

Add `.env` to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# 📄 Adding College Documents

Place your college PDFs inside the `data/` directory.

Example:

```text
data/
├── admission.pdf
├── hostel.pdf
├── placements.pdf
├── courses.pdf
└── college_information.pdf
```

The documents become the knowledge source for the RAG pipeline.

---

# ▶️ Running the Application

## Start Streamlit

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## Start FastAPI

```bash
uvicorn api:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

# 🧪 Example Questions

Users can ask questions such as:

```text
What is the admission process?
```

```text
What courses are offered by the college?
```

```text
Tell me about hostel facilities.
```

```text
What is the fee structure?
```

```text
Tell me about placement opportunities.
```

```text
What campus facilities are available?
```

---

# 🛡️ How RAG Helps Reduce Hallucination

A major challenge with LLM-based applications is **hallucination**, where a model may generate information that is not supported by the actual knowledge source.

CampusGPT addresses this by retrieving relevant information from the college document collection and providing that information as context to the LLM.

```text
User Query
    ↓
Retrieve Relevant Documents
    ↓
Provide Retrieved Context to LLM
    ↓
Generate Contextual Answer
```

This makes the system more suitable for institution-specific question answering.

> **Important:** RAG reduces the risk of hallucination but does not guarantee that every generated answer is factually correct. The quality of responses depends on the quality and completeness of the source documents and retrieval pipeline.

---

# 📊 Advantages

* ⚡ Faster access to college information
* 💬 Natural-language interaction
* 🔎 Semantic document retrieval
* 📄 Supports PDF-based knowledge sources
* 🤖 Uses LLMs for contextual responses
* 🧠 Reduces dependence on keyword-based search
* 🏫 Useful for college information assistance
* 🔌 Provides both UI and API access
* 📈 Can be extended with additional institutional data

---

# 🔮 Future Enhancements

### 🌐 Multilingual Support

Allow students to interact with the assistant in multiple Indian languages.

### 🎤 Voice Assistant

Add speech-to-text and text-to-speech capabilities.

### 📱 Mobile Application

Build a mobile version for Android and iOS.

### 🔐 Student Authentication

Provide personalized responses for authenticated students.

### 🗄️ Database Integration

Connect the system with structured student and academic databases.

### 📊 Admin Dashboard

Allow administrators to upload, update, and manage institutional documents.

### 🔔 Notification System

Provide important college announcements and deadline reminders.

### ☁️ Scalable Cloud Deployment

Deploy the complete architecture using scalable cloud infrastructure.

---

# 📚 Key Learning Outcomes

Through this project, I gained practical experience in:

* Retrieval-Augmented Generation
* Large Language Models
* Natural Language Processing
* Semantic Search
* Vector Databases
* Document Embeddings
* Prompt Engineering
* LangChain
* Hugging Face
* FAISS
* FastAPI
* Streamlit
* PDF Processing
* LLM Application Development
* AI Application Deployment

---

# 🎓 Project Highlights

### What makes CampusGPT different?

Instead of building a chatbot that simply generates answers from an LLM, CampusGPT combines:

**Document Knowledge + Semantic Retrieval + LLM Generation**

This creates a more useful architecture for institution-specific question answering.

---

# 👨‍💻 Developer

## Ambika Ramireddy

**B.Tech – Computer Science & Engineering (Data Science)**

Interested in:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Natural Language Processing
* RAG Applications

---

# ⭐ Support the Project

If you find CampusGPT useful:

⭐ Star the repository
🍴 Fork the repository
📢 Share the project

---

# 📜 License

This project is developed for educational and learning purposes.
