import csv
import os

STUDENTS_FILE = os.path.join("data", "students.csv")


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


def list_students():
    file = open(STUDENTS_FILE, "r")
    reader = csv.DictReader(file)

    print("\nStudent Records")
    print("-" * 70)

    for student in reader:
        marks = float(student["marks"])
        print(student["student_id"], student["name"], student["department"], marks, calculate_grade(marks))

    file.close()


def seed_sample_data():
    if not os.path.exists("data"):
        os.makedirs("data")

    file = open(STUDENTS_FILE, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(["student_id", "name", "department", "semester", "marks", "attendance"])
    writer.writerow(["SC001", "Aarav Sharma", "IT", 3, 88, 92])
    writer.writerow(["SC002", "Diya Patel", "CSE", 3, 76, 84])
    writer.writerow(["SC003", "Kabir Rao", "IT", 4, 91, 95])
    file.close()

    print("Sample data created.")

