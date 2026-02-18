# --- DAY 13: DICTIONARY COMPREHENSIONS ---

# The Master Database: Project Names mapped to their total Budgets
projects = {
    "Fintech App": 7500,
    "Brand Identity": 1200,
    "E-commerce Site": 8500,
    "Logo Design": 500,
    "Mobile MVP": 6000
}

# The Premium Filter: 
# Dynamically creating a sub-database of projects worth over $5,000
premium_projects = {
    name: budget for name, budget in projects.items() if budget > 5000
}

# Studio Report
print("--- PROJECT VALUE ANALYSIS ---")
print(f"Total Projects Tracked: {len(projects)}")
print(f"Premium Tier Projects: {premium_projects}")
print(f"Strategic Focus: {list(premium_projects.keys())}")