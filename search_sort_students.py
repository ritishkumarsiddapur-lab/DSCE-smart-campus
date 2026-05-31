import csv
import os

STUDENTS_FILE = os.path.join("data", "students.csv")


def search_students():
    term = input("Search student: ").lower()
    file = open(STUDENTS_FILE, "r")
    reader = csv.DictReader(file)

    for student in reader:
        if term in student["student_id"].lower() or term in student["name"].lower() or term in student["department"].lower():
            print(student["student_id"], student["name"], student["department"], student["marks"])

    file.close()


def sort_students():
    students = []
    file = open(STUDENTS_FILE, "r")
    reader = csv.DictReader(file)

    for student in reader:
        student["marks"] = float(student["marks"])
        students.append(student)

    file.close()

    for i in range(len(students)):
        for j in range(0, len(students) - i - 1):
            if students[j]["marks"] < students[j + 1]["marks"]:
                temp = students[j]
                students[j] = students[j + 1]
                students[j + 1] = temp

    for student in students:
        print(student["student_id"], student["name"], student["marks"])

