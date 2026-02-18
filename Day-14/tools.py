#DAY-14 #tools.py

def generate_invoice(project_name, project_budget):
    """
    Saves a project and budget to database.txt safely.
    """

    try:
        with open("database.txt", "a") as file:
            file.write(f"{project_name} | ${project_budget:,.2f}\n")

        print("\n[SUCCESS]: Project saved safely.")

    except FileNotFoundError:
        print("\n[ERROR]: Database file not found. System could not write data.")


def display_projects():
    """
    Reads and prints all stored projects.
    """

    try:
        print("\n=== STORED PROJECTS ===")
        with open("database.txt", "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("\n[INFO]: No database file found yet.")
        