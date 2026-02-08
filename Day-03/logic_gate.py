project_budget = float(input("What is your budget? "))

if project_budget >= 5000:
    print("High-Priority: Move to Direct Consultation.")
    
elif 2000 <= project_budget < 5000:
    print("Status: Standard Project. Send Automated Onboarding Link.")
    
else:
    print("Status: Small Scale. Refer to Junior Partner or Template Store.")