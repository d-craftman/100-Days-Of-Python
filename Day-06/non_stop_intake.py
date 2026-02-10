# Day 06 – The Non-Stop Intake

studio_queue = []

while True:
    raw_project = input("What project are you working on? ").strip()

    if raw_project.lower() == "exit":
        print("\nApplications have closed!")
        break

    clean_project = raw_project.title()
    studio_queue.append(clean_project)

# Bulk Reporting
print("\nActive Projects Queue:")
for index, project in enumerate(studio_queue, start=1):
    print(f"{index}. {project}")

print("\nSystem Summary:")
print("Active Queue: " + " | ".join(studio_queue))