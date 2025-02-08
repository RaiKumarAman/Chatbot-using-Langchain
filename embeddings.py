import os
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load the extracted course data
with open("data/courses.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

# Initialize Hugging Face embeddings model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS vector database with embeddings
vectorstore = FAISS.from_texts(documents, embedding_model)

# Save FAISS index locally
vectorstore.save_local("faiss_index")

print("Embeddings created and stored in faiss_index.")
