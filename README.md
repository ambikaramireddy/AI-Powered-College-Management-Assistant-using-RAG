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

                    ┌─────────────────────────┐
                    │      COLLEGE PDFs       │
                    │  Rules | Syllabus |     │
                    │  Notices | Regulations  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    Document Loading     │
                    │        (PyPDF)           │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       Chunking           │
                    │  Split documents into    │
                    │     smaller chunks       │
                    │   + Chunk Overlap        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │  Hugging Face Embedding │
                    │         Model            │
                    │  Text → Vector Embedding│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       FAISS Index       │
                    │   Store & Search Vectors│
                    └────────────┬────────────┘
                                 │
                                 │
                  ═══════════════╪════════════════
                           QUERY PHASE
                  ═══════════════╪════════════════
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │        USER QUERY       │
                    │ "What is the attendance │
                    │       requirement?"     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Query Embedding       │
                    │  Question → Vector      │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   FAISS Similarity      │
                    │        Search            │
                    │      Top-K Chunks        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Retrieved Context     │
                    │ Relevant PDF chunks     │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Prompt Construction   │
                    │ Query + Context         │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       LLM               │
                    │ Generate grounded answer│
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     FINAL RESPONSE      │
                    │   Answer to the user    │
                    └─────────────────────────┘




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



# 🔮 Future Enhancements

### 🌐 Multilingual Support

Allow students to interact with the assistant in multiple Indian languages.

### 🎤 Voice Assistant

Add speech-to-text and text-to-speech capabilities.

### 📱 Mobile Application

Build a mobile version for Android and iOS.

### 🔐 Student Authentication

Provide personalized responses for authenticated students.

### 🔔 Notification System

Provide important college announcements and deadline reminders.

### ☁️ Scalable Cloud Deployment

Deploy the complete architecture using scalable cloud infrastructure.
🚧 Challenges & Solutions

The main challenge was improving the relevance and accuracy of retrieved information. Initially, some queries returned partially relevant document chunks.

Solution: I optimized the chunk size and overlap, tuned the Top-K retrieval parameter, and used semantic similarity search with Hugging Face embeddings and FAISS. I also grounded the LLM responses using the retrieved document context.
## 🎯 Conclusion

* Built **CampusGPT**, an AI-powered college management assistant using **RAG**.
* Enables students to access college information through **natural language queries**.
* Retrieves relevant information from **official college PDF documents**.
* Uses **Hugging Face embeddings and FAISS** for semantic search and relevant chunk retrieval.
* Uses **LangChain and LLMs** to generate contextual, document-grounded responses.
* Reduces the time required to manually search through multiple college documents.
* Improved retrieval accuracy through **chunking, chunk overlap, and Top-K tuning**.
* Gained practical experience in **RAG, embeddings, vector search, LangChain, LLM integration, FastAPI, and Streamlit**.
* Provides a foundation for future enhancements such as **multilingual support, voice assistance, authentication, notifications, and cloud scalability**.


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
