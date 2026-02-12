# Day 09: File I/O & Data Persistence

## 🎯 Objectives
- Understand the `open()` function for file management.
- Master file modes: Read (`r`), Write (`w`), and Append (`a`).
- Utilize the `with` statement for secure file handling (Context Managers).

## 🛠️ The Build: Craftroom Archive System
Data that disappears on exit is useless for business. Today’s build for @TheCraftroomStudios implements a **Persistent Archiving System**. Instead of losing client profiles when the script ends, we are now writing our project data to external log files.

### Key Features:
- **Permanent Logging:** Saving client names and budgets to `projects.txt`.
- **Context Management:** Using `with open(...)` to prevent memory leaks and file corruption.
- **Append Logic:** Adding new clients to an existing list without overwriting previous data.

## 🚀 Technical Takeaway
File handling is the first step toward building software that people can actually use over time. Mastering I/O is the difference between a "script" and a "permanent record."

---
*If it isn't saved, it didn't happen.* 🐍💾
