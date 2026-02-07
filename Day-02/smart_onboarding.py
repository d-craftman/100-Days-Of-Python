# Project: Craftroom Smart Onboarding System
# Goal: Data Sanitization and Automated ID Generation

client_name = input("Enter Client Name: ")
industry = input("Enter Industry: ")
budget = float(input("Enter Project Budget ($): "))

# 1. Data Normalization (Cleaning the 'Messy' Input)
clean_name = client_name.strip().title()
clean_industry = industry.strip().upper()

# 2. Logic: Security Deposit (20%) & Project ID
# Slicing [:3] takes the first 3 letters of the industry
deposit = budget * 0.20
project_id = f"{clean_industry[:3]}-{len(clean_name)}"

# 3. System Output (The Professional Dashboard)
print("\n" + "="*40)
print(f"           PROJECT BRIEF")
print("="*40)
print(f"Project ID:       {project_id}")
print(f"Client:           {clean_name}")
print(f"Industry:         {clean_industry}")
print(f"Total Budget:     ${budget:,.2f}")
print(f"Required Deposit: ${deposit:,.2f}")
print("="*40)
print("System Status: Ready for Development 🚀")