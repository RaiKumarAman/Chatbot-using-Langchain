import json
import faiss
import numpy as np
from flask import Flask, render_template, request, jsonify
from langchain.embeddings import HuggingFaceEmbeddings

app = Flask(__name__)

# Load FAISS index and metadata
faiss_index = faiss.read_index("faiss_index.bin")
with open("faiss_metadata.json", "r", encoding="utf-8") as f:
    courses = json.load(f)

# Load Hugging Face embeddings model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def search_courses(query):
    """Search FAISS index for relevant courses"""
    query_embedding = np.array([embedding_model.embed_query(query)], dtype=np.float32)

    # Perform FAISS search
    k = 5  # Number of top results
    distances, indices = faiss_index.search(query_embedding, k)

    # Retrieve matching courses (only exact matches or close matches)
    results = []
    for idx in indices[0]:
        if idx < len(courses):
            course = courses[idx]
            if query.lower() in course["course_name"].lower():  # Exact match based on course name
                results.append(course)
    
    return results

def get_bot_response(query):
    """Handle small talk or simple queries"""
    query = query.lower()

    if "hello" in query or "hi" in query:
        return "Hello! How can I assist you today? 😊"
    elif "how are you" in query:
        return "I'm doing great, thank you for asking! How about you? 😄"
    elif "about" in query or "who are you" in query:
        return "I am your friendly course assistant. I can help you find courses on various topics. Just ask me!"
    elif "help" in query:
        return "I can help you find courses, tell you about them, and more! Just ask me anything related to courses."
    else:
        return None  # If no small talk, let search handle it.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot queries and returns JSON responses"""
    data = request.get_json()
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query cannot be empty"}), 400

    # Small talk or FAQ handling
    response = get_bot_response(query)
    if response:
        return jsonify({"response": [{"text": response}]})

    # Search for courses if it's not small talk
    results = search_courses(query)

    # Format response
    response_data = []
    if results:
        for course in results:
            response_data.append({
                "course_name": course.get("course_name", "N/A"),
                "lesson_count": course.get("lesson_count", "N/A"),
                "price_per_session": course.get("price_per_session", "N/A"),
                "description": course.get("description", "N/A")
            })
        return jsonify({"response": response_data})
    else:
        return jsonify({"response": [{"text": "Sorry, I couldn't find any courses that match your query. 😞"}]})

if __name__ == "__main__":
    app.run(debug=True)
