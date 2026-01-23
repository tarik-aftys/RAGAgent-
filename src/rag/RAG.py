from pathlib import Path
from typing import List, Tuple, Dict, Any
from datetime import date

import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GENERATION_MODEL = "google/flan-t5-base"
DEFAULT_TOP_K = 3

BASE_DIR = Path(__file__).parent.parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
DOCUMENTS_DIR = DATA_DIR / "documents"
QUERIES_DIR = DATA_DIR / "queries"

OUTPUT_TXT = OUTPUT_DIR / "retrieved_context.txt"
OUTPUT_ANSWER = OUTPUT_DIR / "generated_answer.txt"  

class RAGAgent:
    def __init__(self, embedding_model: str = EMBEDDING_MODEL, generation_model: str = GENERATION_MODEL):
        self.embedding_model = SentenceTransformer(embedding_model)
        self.generator = pipeline("text2text-generation", model=generation_model, device=-1)
    
    def embed(self, texts: List[str]) -> np.ndarray:
        embeddings = self.embedding_model.encode(texts, convert_to_numpy=True)
        return embeddings
    
    @staticmethod
    def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
        norm_a = np.linalg.norm(a)
        norm_b = np.linalg.norm(b)
        if norm_a == 0 or norm_b == 0:
            return 0.0
        return np.dot(a, b) / (norm_a * norm_b)
    
    @staticmethod
    def load_documents(doc_paths: List[str] = None) -> List[str]:
        if doc_paths is None:
            doc_paths = [
                str(DOCUMENTS_DIR / "Doc1.txt"),
                str(DOCUMENTS_DIR / "Doc2.txt"),
                str(DOCUMENTS_DIR / "Doc3.txt")
            ]
        
        documents = []
        for path in doc_paths:
            file_path = Path(path)
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:
                        documents.append(content)
        
        if not documents:
            raise ValueError("No valid documents could be loaded")
        
        return documents
    
    @staticmethod
    def load_query(query_path: str = None) -> str:  
        if query_path is None:
            query_path = str(QUERIES_DIR / "query.txt")
        
        file_path = Path(query_path)
        if not file_path.exists():
            raise FileNotFoundError(f"Query file not found: {query_path}")
        
        with open(file_path, "r", encoding="utf-8") as f:
            query = f.read().strip()
            if not query:
                raise ValueError("Query file is empty")
            return query
    
    def retrieve(self, documents: List[str], query: str, top_k: int = DEFAULT_TOP_K) -> List[Tuple[str, float]]:
        if not documents:
            raise ValueError("Documents list cannot be empty")
        if not query:
            raise ValueError("Query cannot be empty")
        
        query_embedding = self.embed([query])[0]
        document_embeddings = self.embed(documents)
        
        scored_documents = [
            (doc.strip(), self.cosine_similarity(query_embedding, doc_emb))
            for doc, doc_emb in zip(documents, document_embeddings)
        ]
        
        scored_documents.sort(key=lambda x: x[1], reverse=True)
        return scored_documents[:top_k]
    
    def generate(self, query: str, context_documents: List[str]) -> str:
        context = "\n".join([f"- {doc}" for doc in context_documents])
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        result = self.generator(prompt, max_length=200, num_return_sequences=1)
        return result[0]["generated_text"].strip()
    
    @staticmethod
    def save_outputs(results: List[Tuple[str, float]], answer: str = None) -> None:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        
        payload: Dict[str, Any] = {
            "date": str(date.today()),
            "results": [
                {"document": doc, "similarity": round(float(score), 3)}
                for doc, score in results
            ]
        }
        
        if answer:
            payload["generated_answer"] = answer
        
        with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
            f.write("Retrieved Context\n")
            f.write("=" * 40 + "\n\n")
            for result in payload["results"]:
                f.write(f"Score: {result['similarity']} — {result['document']}\n")
            if answer:
                f.write("\n" + "=" * 40 + "\n")
                f.write("Generated Answer\n")
                f.write("=" * 40 + "\n\n")
                f.write(answer)
        
        if answer:
            with open(OUTPUT_ANSWER, "w", encoding="utf-8") as f:
                f.write(answer)
    
    def run(self, query_path: str = None, doc_paths: List[str] = None, top_k: int = DEFAULT_TOP_K) -> None:
        documents = self.load_documents(doc_paths)
        query = self.load_query(query_path)
        results = self.retrieve(documents, query, top_k)
        retrieved_docs = [doc for doc, _ in results]
        answer = self.generate(query, retrieved_docs)
        self.save_outputs(results, answer)

def main():
    agent = RAGAgent()
    agent.run()

if __name__ == "__main__":
    main()