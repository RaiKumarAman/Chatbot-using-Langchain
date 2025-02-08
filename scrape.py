import os
from langchain.document_loaders import WebBaseLoader

# Load website content
loader = WebBaseLoader("https://brainlox.com/courses/category/technical")
docs = loader.load()

# Extract raw text
documents = [doc.page_content for doc in docs]

# Ensure the 'data/' directory exists
os.makedirs("data", exist_ok=True)

# Save extracted data to a text file
with open("data/courses.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(documents))

print(f"Extracted {len(documents)} course descriptions and saved to data/courses.txt.")
