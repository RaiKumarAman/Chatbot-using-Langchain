import json
import faiss
import numpy as np
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load structured courses data
with open("structured_courses.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Initialize Hugging Face embeddings model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Extract descriptions and generate embeddings
descriptions = [course["description"] for course in courses]
embeddings = embedding_model.embed_documents(descriptions)

# Convert embeddings to FAISS format
embedding_dim = len(embeddings[0])
faiss_index = faiss.IndexFlatL2(embedding_dim)
faiss_index.add(np.array(embeddings, dtype=np.float32))

# Save FAISS index
faiss.write_index(faiss_index, "faiss_index.bin")

# Save metadata (mapping index to course details)
with open("faiss_metadata.json", "w", encoding="utf-8") as f:
    json.dump(courses, f, indent=4)

print(f"Stored {len(courses)} courses in FAISS index.")
