import tools

def run_studio():
    try:
        project_name = input("Enter Project Name: ").strip().title()
        project_budget = float(input("Enter Project Budget: "))

        tools.generate_invoice(project_name, project_budget)

    except ValueError:
        print("\n[ERROR]: Invalid budget format. Please enter numbers only.")

    tools.display_projects()

if __name__ == "__main__":
    run_studio()