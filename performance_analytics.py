import os


def generate_analytics():
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        import pandas as pd
    except:
        print("Please install numpy, pandas and matplotlib.")
        return

    file_name = os.path.join("data", "students.csv")

    if not os.path.exists(file_name):
        print("Student file not found.")
        return

    df = pd.read_csv(file_name)
    marks = df["marks"].to_numpy()

    print("Average marks:", np.mean(marks))
    print("Highest marks:", np.max(marks))
    print("Lowest marks:", np.min(marks))

    plt.bar(df["name"], df["marks"])
    plt.title("Student Performance")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(os.path.join("reports", "student_performance.png"))
    plt.close()

    print("Chart saved.")

