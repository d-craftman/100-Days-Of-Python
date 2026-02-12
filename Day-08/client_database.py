# Project: Craftroom Client Database
# Purpose: Implementing Key-Value architectures for project metadata
# Day: 08 of 100

# 1. Structured Data Intake
project_profile = {
    "name": input("Input Client Name: ").strip(),
    "industry": input("Industry: ").strip(),
    "budget": float(input("Project Budget ($): ")),
    "status": "Lead" # Default status
}

# 2. State Management (Updating the Database)
# Moving the project from Lead to Active
project_profile.update({
    "status": "Onboarded",
    "deposit_paid": True
})

# 3. Dynamic Data Retrieval
# We pull data directly from the dictionary to ensure accuracy
print(f"\n[SYSTEM LOG]: Client {project_profile['name'].title()} "
      f"({project_profile['industry'].title()}) registered successfully.")

# 4. Interactive Enquiry System
# Using .upper() to handle lowercase inputs like 's' or 'b'
query = input("\nEnter Enquiry Code (S = Status, B = Budget): ").strip().upper()

if query == "S":
    result = project_profile.get("status", "N/A")
    print(f">> PROJECT STATUS: {result}")
elif query == "B":
    result = project_profile.get("budget", 0)
    print(f">> PROJECT BUDGET: ${result:,.2f}")
else:
    print(">> ALERT: Invalid Enquiry Code. No request processed.")

# Final Dashboard View for GitHub
print("\n--- Current Data Object ---")
print(project_profile)