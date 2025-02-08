import re
import json

# Load scraped content from courses.json
with open("courses.json", "r", encoding="utf-8") as f:
    scraped_content = f.read()

# Updated Regular Expression to handle multiline descriptions, and more complex course names
pattern = re.compile(
    r"(?P<course_name>LEARN [^\n]+(?:-[^\n]+)?)\s*"  # Capture full course name, including potential hyphens in course names
    r"(?P<description>.+?)\s*"  # Capture the description text, spanning multiple lines
    r"(?P<lesson_count>\d+ Lessons).*?"  # Capture lesson count (e.g., "18 Lessons")
    r"\$(?P<price>\d+)",  # Capture price (e.g., "$30")
    re.DOTALL  # Make dot match newlines as well
)

# Extract courses using the updated regex
matches = pattern.finditer(scraped_content)

# Process extracted data into structured format
courses = []
for match in matches:
    course_data = {
        "course_name": match.group("course_name").strip(),
        "lesson_count": match.group("lesson_count").strip(),
        "price_per_session": f"${match.group('price')}",
        "description": match.group("description").strip()
    }
    courses.append(course_data)

# Save extracted courses as JSON
with open("structured_courses.json", "w", encoding="utf-8") as f:
    json.dump(courses, f, indent=4)

# Print structured courses
for course in courses:
    print(f"\nCourse Name: {course['course_name']}")
    print(f"Lesson Count: {course['lesson_count']}")
    print(f"Price per Session: {course['price_per_session']}")
    print(f"Description: {course['description']}")
