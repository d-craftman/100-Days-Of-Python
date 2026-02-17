# --- DAY 10: EXCEPTION HANDLING (TRY/EXCEPT) ---

try:
    project_name = input("Enter Project Name: ").strip().title()
    # If the user enters a non-number here, the code jumps straight to 'except'
    project_budget = float(input("Enter Project Budget: "))

    with open("database.txt", "a") as file:
        file.write(f"{project_name} | ${project_budget:,.2f}\n")
    
    print("\n[SUCCESS]: Project saved safely.")

except ValueError:
    # This catches typos like entering 'Ten Thousand' instead of 10000
    print("\n[ERROR]: Invalid budget format. Please enter numbers only (e.g., 5000).")

except FileNotFoundError:
    print("\n[ERROR]: Database file not found. System could not write data.")

# Final check to see the data (Only if the file actually exists)
print("\n=== STORED PROJECTS ===")
with open("database.txt", "r") as file:
    for line in file:
        print(line.strip())