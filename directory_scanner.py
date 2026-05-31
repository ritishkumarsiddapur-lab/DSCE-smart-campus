import os


def scan_directory():
    path = input("Enter directory path: ")

    if not os.path.exists(path):
        print("Directory not found.")
        return

    files = os.listdir(path)

    if len(files) == 0:
        print("Folder is empty.")
        return

    for file in files:
        full_path = os.path.join(path, file)

        if os.path.isdir(full_path):
            print("Directory:", file)
        else:
            print("File:", file)

