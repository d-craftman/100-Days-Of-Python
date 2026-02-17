# --- DAY 11: MODULAR EXTENSIONS (DATETIME) ---
import datetime

# Capture the current date and time for the project log
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

try:
    project_name = input("Enter Project Name: ").strip().title()
    project_budget = float(input("Enter Project Budget: "))

    with open("database.txt", "a") as file:
        # We inject the timestamp at the beginning of the line for easy sorting
        file.write(f"[{timestamp}] {project_name} | ${project_budget:,.2f}\n")
    
    print(f"\n[SUCCESS]: Logged at {timestamp}")

except ValueError:
    print("\n[ERROR]: Input error. Project not saved.")

# Verification print
print("\n=== STUDIO AUDIT LOG ===")
with open("database.txt", "r") as file:
    for line in file:
        print(line.strip())