from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Chatbot(Resource):
    def post(self):
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "Query parameter is required."})

        # Load the stored FAISS index
        vectorstore = FAISS.load_local("faiss_index", HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"))

        # Perform similarity search
        results = vectorstore.similarity_search(query, k=3)
        response_texts = [res.page_content for res in results]

        return jsonify({"response": response_texts})

# Add API endpoint
api.add_resource(Chatbot, "/chat")

if __name__ == "__main__":
    app.run(debug=True)
