import csv
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
STUDENTS_FILE = os.path.join(DATA_DIR, "students.csv")
ENROLLMENTS_FILE = os.path.join(DATA_DIR, "enrollments.json")
ACADEMIC_RECORDS_FILE = os.path.join(DATA_DIR, "academic_records.csv")

COURSES = {
    "PY101": {"name": "Python Programming", "credits": 4, "fee": 4500},
    "DB102": {"name": "Database Management", "credits": 3, "fee": 3500},
    "WD103": {"name": "Web Development", "credits": 3, "fee": 4000},
    "AI104": {"name": "AI Fundamentals", "credits": 4, "fee": 5500},
}


def create_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    if not os.path.exists(STUDENTS_FILE):
        file = open(STUDENTS_FILE, "w", newline="")
        writer = csv.writer(file)
        writer.writerow(["student_id", "name", "department", "semester", "marks", "attendance"])
        file.close()

    if not os.path.exists(ENROLLMENTS_FILE):
        file = open(ENROLLMENTS_FILE, "w")
        file.write("{}")
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


def load_students():
    create_files()
    students = []

    file = open(STUDENTS_FILE, "r")
    reader = csv.DictReader(file)

    for row in reader:
        row["semester"] = int(row["semester"])
        row["marks"] = float(row["marks"])
        row["attendance"] = float(row["attendance"])
        students.append(row)

    file.close()
    return students


def save_students(students):
    create_files()

    file = open(STUDENTS_FILE, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=["student_id", "name", "department", "semester", "marks", "attendance"])
    writer.writeheader()

    for student in students:
        writer.writerow(student)

    file.close()


def load_enrollments():
    create_files()

    file = open(ENROLLMENTS_FILE, "r")
    enrollments = json.load(file)
    file.close()

    return enrollments


def save_enrollments(enrollments):
    create_files()

    file = open(ENROLLMENTS_FILE, "w")
    json.dump(enrollments, file, indent=4)
    file.close()


def register_student():
    students = load_students()
    student_id = input("Student ID: ").strip().upper()

    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists.")
            return

    student = {
        "student_id": student_id,
        "name": input("Name: "),
        "department": input("Department: "),
        "semester": input_int("Semester: ", 1, 8),
        "marks": input_float("Overall marks: ", 0, 100),
        "attendance": input_float("Attendance percentage: ", 0, 100),
    }

    students.append(student)
    save_students(students)

    print("Registered", student["name"])
    print("Grade:", calculate_grade(student["marks"]))
    print("Result:", get_result(student["marks"], student["attendance"]))


def show_courses():
    print("\nAvailable Courses")
    print("-" * 60)

    for code in COURSES:
        course = COURSES[code]
        print(code, "-", course["name"], "- Credits:", course["credits"], "- Fee: Rs.", course["fee"])


def enroll_student():
    students = load_students()
    enrollments = load_enrollments()
    student_id = input("Student ID: ").strip().upper()
    found = False

    for student in students:
        if student["student_id"] == student_id:
            found = True

    if found == False:
        print("Student not found.")
        return

    show_courses()
    selected = input("Enter course codes separated by comma: ").upper().replace(" ", "").split(",")

    if student_id not in enrollments:
        enrollments[student_id] = []

    for code in selected:
        if code in COURSES and code not in enrollments[student_id]:
            enrollments[student_id].append(code)

    save_enrollments(enrollments)
    print("Enrollment updated.")


def list_students(students=None):
    if students == None:
        students = load_students()

    if len(students) == 0:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 95)
    print("ID\tName\tDepartment\tSemester\tMarks\tAttendance\tGrade\tResult")
    print("-" * 95)

    for student in students:
        print(
            student["student_id"],
            student["name"],
            student["department"],
            student["semester"],
            student["marks"],
            student["attendance"],
            calculate_grade(student["marks"]),
            get_result(student["marks"], student["attendance"]),
            sep="\t",
        )


def search_students():
    students = load_students()
    term = input("Search by ID, name, or department: ").lower()
    results = []

    for student in students:
        if term in student["student_id"].lower() or term in student["name"].lower() or term in student["department"].lower():
            results.append(student)

    list_students(results)


def sort_students():
    students = load_students()
    print("1. Name")
    print("2. Marks")
    print("3. Attendance")
    print("4. Semester")
    choice = input("Sort by: ")

    for i in range(len(students)):
        for j in range(0, len(students) - i - 1):
            swap = False

            if choice == "1" and students[j]["name"] > students[j + 1]["name"]:
                swap = True
            elif choice == "2" and students[j]["marks"] < students[j + 1]["marks"]:
                swap = True
            elif choice == "3" and students[j]["attendance"] < students[j + 1]["attendance"]:
                swap = True
            elif choice == "4" and students[j]["semester"] > students[j + 1]["semester"]:
                swap = True

            if swap == True:
                temp = students[j]
                students[j] = students[j + 1]
                students[j + 1] = temp

    list_students(students)


def fee_menu():
    enrollments = load_enrollments()
    student_id = input("Student ID: ").strip().upper()

    if student_id not in enrollments:
        print("No enrolled courses found.")
        return

    total = 0
    for code in enrollments[student_id]:
        total = total + COURSES[code]["fee"]

    scholarship = input_float("Scholarship percentage: ", 0, 100)
    discount = total * scholarship / 100

    print("Courses:", ", ".join(enrollments[student_id]))
    print("Total payable fee: Rs.", total - discount)


def add_academic_record():
    students = load_students()
    student_id = input("Student ID: ").strip().upper()
    found = False

    for student in students:
        if student["student_id"] == student_id:
            found = True

    if found == False:
        print("Student not found.")
        return

    show_courses()
    course_code = input("Course code: ").strip().upper()

    if course_code not in COURSES:
        print("Invalid course code.")
        return

    internal = input_float("Internal marks out of 40: ", 0, 40)
    external = input_float("External marks out of 60: ", 0, 60)
    total = internal + external
    grade = calculate_grade(total)

    file = open(ACADEMIC_RECORDS_FILE, "a", newline="")
    writer = csv.writer(file)
    writer.writerow([student_id, course_code, internal, external, total, grade])
    file.close()

    print("Academic record saved.")


def scan_directory():
    path = input("Directory to scan (press Enter for data folder): ")

    if path == "":
        path = DATA_DIR

    if not os.path.exists(path):
        print("Directory not found.")
        return

    items = os.listdir(path)

    if len(items) == 0:
        print("Folder is empty.")
        return

    for item in items:
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            print("Directory:", item)
        else:
            print("File:", item, "-", os.path.getsize(full_path), "bytes")


def generate_analytics():
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
    except:
        print("Please install numpy, pandas and matplotlib.")
        return

    students = load_students()

    if len(students) == 0:
        seed_sample_data()
        students = load_students()

    names = []
    marks = []

    for student in students:
        names.append(student["name"])
        marks.append(student["marks"])

    marks_array = np.array(marks)

    print("Average marks:", np.mean(marks_array))
    print("Highest marks:", np.max(marks_array))
    print("Lowest marks:", np.min(marks_array))

    df = pd.DataFrame(students)
    print(df.groupby("department")["marks"].mean())

    chart_path = os.path.join(REPORTS_DIR, "student_performance.png")
    plt.bar(names, marks)
    plt.title("Student Performance")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()

    print("Chart saved at:", chart_path)


def seed_sample_data():
    students = [
        {"student_id": "SC001", "name": "Aarav Sharma", "department": "IT", "semester": 3, "marks": 88, "attendance": 92},
        {"student_id": "SC002", "name": "Diya Patel", "department": "CSE", "semester": 3, "marks": 76, "attendance": 84},
        {"student_id": "SC003", "name": "Kabir Rao", "department": "IT", "semester": 4, "marks": 91, "attendance": 95},
        {"student_id": "SC004", "name": "Meera Nair", "department": "AIML", "semester": 2, "marks": 67, "attendance": 78},
        {"student_id": "SC005", "name": "Rohan Gupta", "department": "CSE", "semester": 4, "marks": 39, "attendance": 72},
    ]

    enrollments = {
        "SC001": ["PY101", "DB102"],
        "SC002": ["PY101", "WD103"],
        "SC003": ["AI104", "PY101"],
        "SC004": ["DB102", "WD103"],
        "SC005": ["PY101"],
    }

    save_students(students)
    save_enrollments(enrollments)
    print("Sample data created.")


def show_summary():
    students = load_students()
    enrollments = load_enrollments()

    print("Students registered:", len(students))

    total_enrollments = 0
    for student_id in enrollments:
        total_enrollments = total_enrollments + len(enrollments[student_id])

    print("Total enrollments:", total_enrollments)


def menu():
    create_files()

    while True:
        print("\nSmart Campus Information System")
        print("=" * 40)
        print("1. Student registration and grade evaluation")
        print("2. Course enrollment management")
        print("3. Student record storage and management")
        print("4. Search student data")
        print("5. Sort student data")
        print("6. Fee calculation")
        print("7. File-based academic record management")
        print("8. Directory scanning with exception handling")
        print("9. Student performance analytics")
        print("10. Create sample data")
        print("11. Show campus summary")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            register_student()
        elif choice == "2":
            enroll_student()
        elif choice == "3":
            list_students()
        elif choice == "4":
            search_students()
        elif choice == "5":
            sort_students()
        elif choice == "6":
            fee_menu()
        elif choice == "7":
            add_academic_record()
        elif choice == "8":
            scan_directory()
        elif choice == "9":
            generate_analytics()
        elif choice == "10":
            seed_sample_data()
        elif choice == "11":
            show_summary()
        elif choice == "0":
            print("Thank you for using Smart Campus Information System.")
            break
        else:
            print("Invalid choice.")


menu()

