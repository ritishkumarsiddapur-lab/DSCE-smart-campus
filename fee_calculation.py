COURSES = {
    "PY101": {"name": "Python Programming", "fee": 4500},
    "DB102": {"name": "Database Management", "fee": 3500},
    "WD103": {"name": "Web Development", "fee": 4000},
    "AI104": {"name": "AI Fundamentals", "fee": 5500},
}


def calculate_fee():
    total = 0

    while True:
        code = input("Enter course code (or done): ").upper()

        if code == "DONE":
            break

        if code in COURSES:
            total = total + COURSES[code]["fee"]
        else:
            print("Invalid course code.")

    scholarship = float(input("Scholarship percentage: "))
    discount = total * scholarship / 100
    final_amount = total - discount

    print("Total fee:", total)
    print("Discount:", discount)
    print("Final amount:", final_amount)


calculate_fee()

