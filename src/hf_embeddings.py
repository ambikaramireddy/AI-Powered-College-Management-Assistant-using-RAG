import os
from typing import List
import numpy as np
from huggingface_hub import InferenceClient

class HFEmbeddings:

    def __init__(self):

        token = os.getenv("HF_TOKEN")

        if not token:
            raise ValueError("HF_TOKEN missing")

        self.model = os.getenv(
            "HF_EMBEDDING_MODEL",
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        # REMOVE provider="hf-inference"
        self.client = InferenceClient(
            api_key=token
        )

    def embed_documents(self, texts: List[str]) -> np.ndarray:

        vectors = self.client.feature_extraction(
            texts,
            model=self.model
        )

        arr = np.array(vectors, dtype="float32")

        if arr.ndim == 1:
            arr = arr.reshape(1, -1)

        return arr

    def embed_query(self, text: str) -> np.ndarray:

        vector = self.client.feature_extraction(
            text,
            model=self.model
        )

        arr = np.array(vector, dtype="float32")

        if arr.ndim > 1:
            arr = arr[0]

        return arr.reshape(1, -1)