# Project: Craftroom Studio Queue Manager
# Purpose: Manage multiple project streams using Python Lists
# Day: 05 of 100

# 1. Initialize the project registry
# We start with our current active workload
active_projects = ["Fintech App", "Fashion Brand", "E-com Site"]

print(f"DEBUG: System initialized. Current load: {len(active_projects)} projects.")

# 2. Workflow Simulation (Cleaning up completed tasks)
# Removing 'Fashion Brand' (Index 1) 
active_projects.pop(1)
# Removing 'E-com Site' by specifically calling the name
active_projects.remove("E-com Site")

# 3. Dynamic Client Intake
# We sanitize input immediately to keep the data clean
new_client_project = input("\n>>> Enter New Project Name: ").strip().title()

# Logic: Add the new project to our collection
active_projects.append(new_client_project)

# 4. Data Optimization
# Sorting alphabetically for a professional dashboard view
active_projects.sort()

# 5. Professional Dashboard Output
print("\n" + "—"*40)
print(f"      CRAFTROOM STUDIOS | PROJECT QUEUE")
print("—"*40)
print(f"TOTAL ACTIVE SLOTS: {len(active_projects)}")
print(f"CURRENT PIPELINE:   {' | '.join(active_projects)}")
print("—"*40)
print("STATUS: Queue Optimized | Ready for Next step")