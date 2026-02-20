import tools

def run_studio():
    print("--- CRAFTROOM STUDIO OS (v2.0) ---")
    
    try:
        # 1. Intake
        name = input("Project Name: ").strip().title()
        budget = float(input("Budget ($): "))

        # 2. Save via JSON Engine
        tools.generate_invoice(name, budget)

        # 3. Report
        tools.display_projects()
        
        # 4. Financial Insight
        total = tools.calculate_total_revenue()
        print(f"\nTOTAL PIPELINE VALUE: ${total:,.2f}")

    except ValueError:
        print("\n[ERROR]: Please enter a valid number for the budget.")

if __name__ == "__main__":
    run_studio()