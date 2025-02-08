import requests
from bs4 import BeautifulSoup

def fetch_course_data():
    url = "https://brainlox.com/courses/category/technical"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract course titles (example: modify this as needed based on the page structure)
    courses = []
    course_elements = soup.find_all('h2', class_='entry-title')  # Adjust this based on the webpage's structure

    for element in course_elements:
        courses.append(element.get_text(strip=True))
    
    return courses
