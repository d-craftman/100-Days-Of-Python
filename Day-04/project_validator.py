# Project:  Advanced Project Validator
# Goal: Use Logical Operators (AND/OR) for complex decision making

print("---    Project Validator ---")

budget = float(input("Enter Project Budget ($): "))
is_referral = input("Is this a VIP referral? (yes/no): ").strip().lower()
is_urgent = input("Is this an urgent delivery? (yes/no): ").strip().lower()

# Day 04 Logic: Multi-Factor Decision Making
# Rule 1: VIPs or Big Budgets get immediate access
if budget >= 5000 or is_referral == "yes":
    status = "VIP PRIORITY"
    action = "Direct Founder Consultation"

# Rule 2: Mid-range projects that aren't rushing are Standard
elif budget >= 2000 and is_urgent == "no":
    status = "STANDARD"
    action = "Automated Onboarding Pipeline"

# Rule 3: Mid-range but URGENT projects need a surcharge
elif budget >= 2000 and is_urgent == "yes":
    status = "STANDARD - URGENT"
    action = "Apply 25% Expedited Fee & Notify Team"

else:
    status = "REJECTED/REFERRAL"
    action = "Send to Junior Partner Network"

print("\n" + "="*40)
print(f"VALDIATION RESULT: {status}")
print(f"NEXT STEP:         {action}")
print("="*40)