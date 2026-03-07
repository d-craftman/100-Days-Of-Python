# Day 32: Encapsulation & Instance Methods

## 🎯 Objectives
- Implement Class Methods to handle internal logic.
- Master the `self` keyword to access object attributes.
- Practice "Encapsulation" by bundling data and behavior together.

## 🛠️ The Build: Self-Managing Projects
A project at @TheCraftroomStudios should know its own value. Today, we upgraded our `Project` class. Instead of using outside math, every project now has a `.get_total_cost()` method that automatically adds service fees and taxes to the base budget.

### Key Features:
- **Internal Logic:** Methods defined inside the class to process object data.
- **The `self` Power:** Using `self` to ensure the method acts on the specific project being called.
- **Clean API:** Reducing the complexity of `main.py` by letting the objects do the heavy lifting.

## 🚀 Technical Takeaway
Methods are what turn a "Data Container" into a "Smart Object." By encapsulating logic within the class, we make our code more modular and much easier to debug.

---
*If an object can do it itself, don't do it for them.* 🐍⚙️
