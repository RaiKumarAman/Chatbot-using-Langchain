# Course Scraping Project

This project scrapes course data from the Brainlox website, generates embeddings for the course descriptions using Hugging Face transformers, and stores the embeddings in a FAISS vector store for fast querying. Additionally, it exposes a Flask API that allows users to query course details based on keywords.

## Project Overview

- **Scraping**: Extracts course names, lesson counts, prices, and descriptions from the Brainlox technical courses page.
- **Embedding**: Uses Hugging Face's transformers to generate embeddings from course descriptions.
- **Querying**: Stores embeddings in a FAISS vector store and provides a RESTful API using Flask to query courses by name or description.

## Project Structure

/course-scraping-project ├── scrape.py # Scraping logic to extract course data ├── embedding.py # Generates embeddings for course descriptions ├── app.py # Flask app to serve queries to the user ├── courses.json # Saved course data after scraping ├── faiss_vector_store # FAISS vector store containing course embeddings └── README.md # Project documentation


## Features

- **Web Scraping**: Scrapes courses from the Brainlox website.
- **Course Embedding**: Converts course descriptions into embeddings using Hugging Face models.
- **Fast Querying**: Stores the embeddings in a FAISS vector store for quick and efficient searching.
- **Flask API**: A RESTful API to interact with the stored course data.

## Requirements

- Python 3.x
- `requests`
- `beautifulsoup4`
- `torch`
- `transformers`
- `faiss-cpu`
- `flask`
- `langchain`

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/your-username/course-scraping-project.git
cd course-scraping-project


### How to Create the `README.md` File:

1. **Create the `README.md` file** in your project directory.
2. **Copy and paste** the above content into the file.
3. **Commit and push** the `README.md` file to your GitHub repository if needed:

```bash
git add README.md
git commit -m "Added README file"
git push origin main
