from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from scraper import fetch_course_data  # Import the scraper function

# Initialize the Hugging Face embeddings model
embedding_model = HuggingFaceEmbeddings()

def create_embeddings():
    # Fetch the course data from the web scraper
    courses = fetch_course_data()

    # Split the data into chunks for better embedding generation
    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=0)
    documents = text_splitter.split_text("\n".join(courses))
    
    # Embed the documents using the HuggingFace embeddings model
    embeddings = embedding_model.embed_documents(documents)  # Apply embedding to documents
    
    # Create and store in FAISS vector store
    vector_store = FAISS.from_documents(documents, embeddings)
    
    # Save the vector store locally for later use
    vector_store.save_local("faiss_vector_store")
    
    return vector_store

if __name__ == "__main__":
    create_embeddings()
