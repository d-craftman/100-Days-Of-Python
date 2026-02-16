# --- DAY 09: FILE I/O (APPEND & READ) ---

# 1. Input Collection
# Strip and Title-case ensure the database stays visually consistent
project_name = input("Enter Project Name: ").strip().title()
project_budget = float(input("Enter Project Budget: "))

# 2. Storage Phase (Append Mode)
# Using 'with' handles the file closing automatically, preventing memory leaks
with open("database.txt", "a") as file:
    file.write(f"{project_name} | ${project_budget:,.2f}\n")

print("\n[SUCCESS]: Project archived in database.\n")

# 3. Verification Phase
# Reading the file back to ensure the data was written correctly
print("=== CURRENT STORED PROJECTS ===")
with open("database.txt", "r") as file:
    for line in file:
        print(line.strip())