# Day 37: Class Methods & Static Methods

## 🎯 Objectives
- Understand the difference between Instance, Class, and Static methods.
- Use `@classmethod` to track studio-wide data (like total project counts).
- Use `@staticmethod` for utility functions that don't need object data.

## 🛠️ The Build: Studio Utilities & Global Tracking
Today at @TheCraftroomStudios, we added a "Utility Belt" to our system. We implemented a `@staticmethod` to validate project names and a `@classmethod` to act as a factory for creating projects from raw data strings.

### Key Features:
- **@staticmethod:** Created a `validate_budget()` helper. It doesn't need to know about "Project A" or "Project B"—it just checks if a number is valid.
- **@classmethod:** Created a `from_string()` constructor. This allows us to take a raw line of text (like from a CSV or log file) and instantly turn it into a Project object.
- **Class State:** Tracking how many total projects the Studio has ever created, regardless of which list they are in.

## 🚀 Technical Takeaway
Static and Class methods help keep your code organized. They prevent "Utility" functions from floating around your files by anchoring them to the classes they relate to.

---
*Clean code isn't just about what it does; it's about where it lives.* 🐍🛠️
