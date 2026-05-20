from pathlib import Path
from typing import List, Dict
import numpy as np
import faiss

from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.hf_embeddings import HFEmbeddings

class Retriever:
    def __init__(self, index, documents, embedder):
        self.index = index
        self.documents = documents
        self.embedder = embedder

    def retrieve(self, query, top_k=5):
        qvec = self.embedder.embed_query(query)

        distances, indices = self.index.search(qvec, top_k)

        results = []

        for idx in indices[0]:
            if idx == -1:
                continue

            results.append(self.documents[idx])

        return results


def extract_pdf_pages(pdf_path: Path):
    reader = PdfReader(str(pdf_path))

    pages = []

    for page_num, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        if text.strip():
            pages.append({
                "source": pdf_path.name,
                "page": page_num,
                "text": text
            })

    return pages


def get_retriever(data_dir="data"):
    data_path = Path(data_dir)

    pdf_files = list(data_path.glob("*.pdf"))

    raw_pages = []

    for pdf in pdf_files:
        raw_pages.extend(extract_pdf_pages(pdf))

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=120
    )

    chunks = []

    for page in raw_pages:
        texts = splitter.split_text(page["text"])

        for chunk in texts:
            chunks.append({
                "source": page["source"],
                "page": page["page"],
                "text": chunk
            })

    embedder = HFEmbeddings()

    embeddings = embedder.embed_documents(
        [c["text"] for c in chunks]
    )

    dim = embeddings.shape[1]

    index = faiss.IndexFlatL2(dim)

    index.add(np.asarray(embeddings, dtype="float32"))

    return Retriever(
        index=index,
        documents=chunks,
        embedder=embedder
    )