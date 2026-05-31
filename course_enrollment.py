import json
import os

DATA_DIR = "data"
STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")
ENROLLMENTS_FILE = os.path.join(DATA_DIR, "enrollments.json")

COURSES = {
    "PY101": {"name": "Python Programming", "credits": 4, "fee": 4500},
    "DB102": {"name": "Database Management", "credits": 3, "fee": 3500},
    "WD103": {"name": "Web Development", "credits": 3, "fee": 4000},
    "AI104": {"name": "AI Fundamentals", "credits": 4, "fee": 5500},
}


def show_courses():
    print("\nAvailable Courses")
    for code in COURSES:
        course = COURSES[code]
        print(code, "-", course["name"], "- Credits:", course["credits"])


def enroll_student():
    if not os.path.exists(ENROLLMENTS_FILE):
        file = open(ENROLLMENTS_FILE, "w")
        file.write("{}")
        file.close()

    file = open(ENROLLMENTS_FILE, "r")
    enrollments = json.load(file)
    file.close()

    student_id = input("Student ID: ").strip().upper()
    show_courses()
    selected = input("Enter course codes separated by comma: ").upper().replace(" ", "").split(",")

    enrollments[student_id] = []

    for code in selected:
        if code in COURSES:
            enrollments[student_id].append(code)

    file = open(ENROLLMENTS_FILE, "w")
    json.dump(enrollments, file, indent=4)
    file.close()

    print("Enrollment saved.")

