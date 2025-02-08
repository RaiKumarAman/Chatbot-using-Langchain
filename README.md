Course Scraping Project
This project scrapes course data from the Brainlox website, generates embeddings for the course descriptions using Hugging Face transformers, and stores the embeddings in a FAISS vector store for fast querying. Additionally, it exposes a Flask API that allows users to query course details based on keywords.

Project Structure
bash
Copy
Edit
/course-scraping-project
├── scrape.py                # Scraping logic to extract course data
├── embedding.py             # Generates embeddings for course descriptions
├── app.py                   # Flask app to serve queries to the user
├── courses.json             # Saved course data after scraping
├── faiss_vector_store       # FAISS vector store containing course embeddings
└── README.md                # Project documentation
Features
Scraping: Extracts course names, lesson counts, prices, and descriptions from the Brainlox technical courses page.
Embedding: Uses Hugging Face's transformers to generate embeddings from course descriptions.
Querying: Stores embeddings in a FAISS vector store and provides a RESTful API using Flask to query courses by name or description.
Requirements
Python 3.x
requests
beautifulsoup4
torch
transformers
faiss-cpu
flask
langchain
webdriver-manager (if using Selenium for scraping dynamic content)
Setup
Clone the repository:
bash
Copy
Edit
git clone https://github.com/your-username/course-scraping-project.git
cd course-scraping-project
Create a virtual environment (optional but recommended):
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install the dependencies:
bash
Copy
Edit
pip install -r requirements.txt
Usage
Step 1: Scrape Course Data
Run scrape.py to scrape course data from the Brainlox website and save it to courses.json:

bash
Copy
Edit
python scrape.py
This will create a courses.json file containing the course information.

Step 2: Generate Embeddings and Store in FAISS Vector Store
Run embedding.py to generate embeddings for course descriptions and store them in a FAISS vector store:

bash
Copy
Edit
python embedding.py
This will create the FAISS vector store file (faiss_vector_store) which will be used for querying.

Step 3: Start the Flask API
Run app.py to start the Flask API server. This will allow you to query the course data via HTTP requests.

bash
Copy
Edit
python app.py
The Flask app will be running at http://127.0.0.1:5000.

Step 4: Querying Courses
You can query the API by sending a GET request to the /query endpoint with a query parameter:

Example query:

bash
Copy
Edit
http://127.0.0.1:5000/query?query=LEARN MOBILE DEVELOPMENT
This will return the course details (name, lesson count, price, description) for the course related to "LEARN MOBILE DEVELOPMENT."

Project Flow
scrape.py:

Scrapes course data from the Brainlox website.
Saves the data in courses.json.
embedding.py:

Loads the scraped data from courses.json.
Generates embeddings for the course descriptions using Hugging Face.
Saves the embeddings in a FAISS vector store.
app.py:

Hosts a Flask API for querying courses.
Uses the FAISS vector store for fast similarity-based querying.
License
This project is licensed under the MIT License - see the LICENSE file for details.
