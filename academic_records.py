import csv
import os

ACADEMIC_RECORDS_FILE = os.path.join("data", "academic_records.csv")


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


def add_academic_record():
    student_id = input("Student ID: ").upper()
    course_code = input("Course code: ").upper()
    internal = float(input("Internal marks out of 40: "))
    external = float(input("External marks out of 60: "))
    total = internal + external
    grade = calculate_grade(total)

    if not os.path.exists("data"):
        os.makedirs("data")

    file = open(ACADEMIC_RECORDS_FILE, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([student_id, course_code, internal, external, total, grade])
    file.close()

    print("Academic record saved.")

