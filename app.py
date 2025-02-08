import os
import re
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings

app = Flask(__name__)
api = Api(app)

class Chatbot(Resource):
    def post(self):
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query parameter is required."})

        # Load FAISS vector store
        vectorstore = FAISS.load_local("faiss_index", HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"), allow_dangerous_deserialization=True)

        # Perform similarity search on the FAISS index
        results = vectorstore.similarity_search(query, k=3)  # k=3 means top 3 results
        
        # Process the results
        response_texts = []

        for res in results:
            # Clean and split the result text (you can adjust the regex based on the structure)
            cleaned_text = res.page_content.strip()

            # Use regex to remove unwanted parts like 'LessonsView Details' and prices
            cleaned_text = re.sub(r'(LessonsView Details.*?)(\d{1,2} Lessons|[\$\d]+)', '', cleaned_text)
            
            response_texts.append(cleaned_text)

        return jsonify({"response": response_texts})

# Add API endpoint
api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    # Run Flask API in background so we can interact with it
    from threading import Thread
    def run_flask():
        app.run(debug=True, use_reloader=False)  # Ensure Flask runs only once
    
    # Start Flask in a separate thread
    thread = Thread(target=run_flask)
    thread.start()

    # Run the command-line interaction
    while True:
        query = input("Enter your query (or type 'exit' to quit): ").strip()

        if query.lower() == 'exit':
            print("Exiting the program.")
            break

        # Send the query to the Flask API (using requests)
        import requests
        response = requests.post("http://127.0.0.1:5000/chat", json={"query": query})
        
        # Get and display the response
        if response.status_code == 200:
            result = response.json()
            print("Response from API:")
            for idx, res in enumerate(result.get("response", [])):
                print(f"{idx+1}. {res}")
        else:
            print(f"Error: {response.status_code}")
