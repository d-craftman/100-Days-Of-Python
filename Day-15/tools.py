#DAY-15 # tools.py

import json
import os


def generate_invoice(project_name, project_budget):
    """
    Saves project data as structured JSON.
    """

    new_project = {
        "name": project_name,
        "budget": project_budget
    }

    # Step 1: Load existing data (if file exists)
    if os.path.exists("database.json"):
        with open("database.json", "r") as file:
            data = json.load(file)
    else:
        data = []

    # Step 2: Append new project
    data.append(new_project)

    # Step 3: Write updated list back to file
    with open("database.json", "w") as file:
        json.dump(data, file, indent=4)

    print("\n[SUCCESS]: Project saved to JSON database.")


def display_projects():
    """
    Reads and prints structured project data.
    """

    if not os.path.exists("database.json"):
        print("\n[INFO]: No database found yet.")
        return

    with open("database.json", "r") as file:
        data = json.load(file)

    print("\n=== STORED PROJECTS (JSON) ===")
    for index, project in enumerate(data, start=1):
        print(f"{index}. {project['name']} - ${project['budget']:,.2f}")


def calculate_total_revenue():
    """
    Calculates total revenue from all stored projects.
    """

    if not os.path.exists("database.json"):
        return 0

    with open("database.json", "r") as file:
        data = json.load(file)

    total = sum(project["budget"] for project in data)
    return total
    