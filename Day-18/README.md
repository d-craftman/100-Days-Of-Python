# Day 18: Input Validation & Data Sanitization

## 🎯 Objectives
- Implement robust data validation for user inputs.
- Create reusable validation functions to keep `main.py` clean.
- Ensure data integrity before writing to the JSON database.

## 🛠️ The Build: The Craftroom "Gatekeeper"
Bad data in equals bad data out. Today’s build for @TheCraftroomStudios introduces a **Validation Layer**. Before a project name or budget is saved, it must pass through our "Gatekeeper" logic to ensure names aren't empty and budgets aren't negative or unrealistic.

### Key Features:
- **Empty String Protection:** Preventing the creation of "Ghost Projects" with no names.
- **Budget Range Checks:** Ensuring project budgets fall within a realistic studio range (e.g., $100 - $1,000,000).
- **Format Consistency:** Automatically cleaning whitespace and casing before the data hits the disk.

## 🚀 Technical Takeaway
Validation is the difference between a prototype and production-ready software. By sanitizing inputs, we protect our database from corruption and ensure our financial reports (Total Revenue) are always accurate.

---
*Trust, but verify.* 🐍🛡️
