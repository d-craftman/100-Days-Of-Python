# Day 33: OOP Pillars — Inheritance

## 🎯 Objectives
- Understand the Parent-Child relationship in classes.
- Use the `super()` function to extend parent functionality.
- Create specialized subclasses for different studio departments.

## 🛠️ The Build: Departmental Subclasses
Efficiency is about not repeating code. Today, we’ve refactored @TheCraftroomStudios to use **Inheritance**. We have a base `Project` class, but we’ve now birthed two specialized children: `WebProject` and `DesignProject`. The `WebProject` automatically tracks URL and Hosting status, while the `DesignProject` tracks Print vs. Digital assets—all while sharing the core Budget and Name logic of the parent.

### Key Features:
- **The Parent Class:** Storing universal data (Name, Budget).
- **Subclassing:** Creating specialized versions of projects without rewriting core logic.
- **Method Overriding:** Customizing how a child object behaves compared to its parent.

## 🚀 Technical Takeaway
Inheritance allows for "DRY" (Don't Repeat Yourself) code at scale. It lets you build a general system and then specialize it for specific business needs as the studio grows.

---
*Build the foundation once; specialize forever.* 🐍🏗️
