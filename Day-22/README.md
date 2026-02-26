# Day 22: Code Refactoring & Helper Functions (DRY Principle)

## 🎯 Objectives
- Apply the **DRY** (Don't Repeat Yourself) principle to the codebase.
- Create private "Helper Functions" to handle repetitive file operations.
- Centralize configurations (like filenames) to a single source of truth.

## 🛠️ The Build: Craftroom Core Refactor
Good code isn't just about what the user sees; it's about how easy it is to maintain. Today at @TheCraftroomStudios, we are refactoring our `tools.py`. Instead of writing `with open(...)` in every function, we are building two master helpers: `load_db()` and `save_db()`. This makes our logic cleaner, shorter, and less prone to bugs.

### Key Features:
- **Centralized File Path:** One variable to rule them all. Change the filename once, and the whole system updates.
- **Unified Loading:** A single function that handles `os.path.exists` checks for the entire app.
- **Streamlined Save Logic:** Reducing boilerplate code across the library.

## 🚀 Technical Takeaway
Refactoring is a core part of the software lifecycle. Clean code reduces "Technical Debt"—the extra work you have to do later because you wrote messy code today.

---
*Clean the kitchen while you cook, and you'll never have a mess.* 🐍🧹
