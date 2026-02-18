# --- DAY 12: OPTIMIZED DATA FILTERING (LIST COMPREHENSIONS) ---

# The raw data: All incoming project inquiries
all_budgets = [1200, 5500, 8000, 1500, 3000]

# The "VIP Filter": Extracting high-value projects in a single Pythonic line
# This replaces a bulky 4-line for loop with efficient logic
vip_projects = [b for b in all_budgets if b >= 5000]

# Outputting the results for the Studio Dashboard
print("--- CRAFTROOM PORTFOLIO ANALYSIS ---")
print(f"Full Budget List: {all_budgets}")
print(f"High-Value Leads: {vip_projects}")
print(f"Status: {len(vip_projects)} VIP projects identified.")