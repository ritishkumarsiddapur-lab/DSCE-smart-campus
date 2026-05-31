import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")
ACADEMIC_RECORDS_FILE = os.path.join(DATA_DIR, "academic_records.csv")

STUDENT_FIELDS = ["student_id", "name", "department", "semester", "marks", "attendance"]


def ensure_storage():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    if not os.path.exists(STUDENTS_FILE):
        file = open(STUDENTS_FILE, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(STUDENT_FIELDS)
        file.close()

    if not os.path.exists(ACADEMIC_RECORDS_FILE):
        file = open(ACADEMIC_RECORDS_FILE, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["student_id", "course_code", "internal_marks", "external_marks", "total", "grade"])
        file.close()


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


def get_result(marks, attendance):
    if marks >= 40 and attendance >= 75:
        return "Pass"
    else:
        return "Needs Improvement"


def load_students():
    ensure_storage()
    students = []

    try:
        file = open(STUDENTS_FILE, "r")
        reader = csv.DictReader(file)

        for row in reader:
            row["semester"] = int(row["semester"])
            row["marks"] = float(row["marks"])
            row["attendance"] = float(row["attendance"])
            students.append(row)

        file.close()
    except:
        print("Could not load student records.")

    return students


def save_students(students):
    ensure_storage()

    file = open(STUDENTS_FILE, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=STUDENT_FIELDS)
    writer.writeheader()

    for student in students:
        writer.writerow(student)

    file.close()


def input_float(message, minimum, maximum):
    while True:
        try:
            value = float(input(message))
            if value >= minimum and value <= maximum:
                return value
            else:
                print("Enter value between", minimum, "and", maximum)
        except:
            print("Enter a valid number.")


def input_int(message, minimum, maximum):
    while True:
        try:
            value = int(input(message))
            if value >= minimum and value <= maximum:
                return value
            else:
                print("Enter value between", minimum, "and", maximum)
        except:
            print("Enter a valid integer.")


def register_student():
    students = load_students()

    student_id = input("Student ID: ").strip().upper()

    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists.")
            return

    student = {
        "student_id": student_id,
        "name": input("Name: ").strip(),
        "department": input("Department: ").strip(),
        "semester": input_int("Semester: ", 1, 8),
        "marks": input_float("Overall marks: ", 0, 100),
        "attendance": input_float("Attendance percentage: ", 0, 100),
    }

    students.append(student)
    save_students(students)

    grade = calculate_grade(student["marks"])
    result = get_result(student["marks"], student["attendance"])

    print("Registered", student["name"])
    print("Grade:", grade)
    print("Result:", result)

