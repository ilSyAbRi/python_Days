# 🌱 Garden Guardian: Agricultural Data Validation – Theory Notes

This document summarizes all the key theory studied so far for handling agricultural data in Python, focusing on error handling and data validation.

---

## 1️⃣ try / except

### Definition
- `try` is a Python keyword that **attempts to run a block of code** that might fail.  
- `except` is a Python keyword that **runs only if an error occurs** in the `try` block.

### Behavior
- If the code in `try` succeeds → `except` is skipped, program continues normally.  
- If the code in `try` fails → Python creates an **exception object**, jumps to `except`, runs its code, and the program continues safely.  

### Purpose
- Allows the program to **handle errors gracefully** without crashing.  
- Ensures that even if invalid input occurs, the program can continue running.

---

## 2️⃣ Exception Objects

### Definition
- An **exception** is a **special object Python creates when an error occurs**.  
- It contains information about **what went wrong**.  

### Key Points
- Exception objects are automatically created by Python when an error occurs.  
- Each exception has a **type** (like `ValueError`) and a **message**.  
- If not handled, the exception will **cause the program to crash**.

---

## 3️⃣ Catching Exceptions

### Definition
- **Catching an exception** means using `except` to handle the exception object.  
- This prevents the program from crashing and allows it to continue safely.

### How It Works
1. Python runs the code in `try`.  
2. If an exception occurs, Python creates an **exception object**.  
3. Python passes the exception object to `except`.  
4. If the type matches the exception in `except`, the code inside `except` runs.  
5. After `except` finishes, the program continues normally.

### Example Types of Exceptions Studied
- `ValueError` → occurs when a function receives an invalid value, e.g., `int("abc")`.  

---

## 4️⃣ ValueError

### Definition
- `ValueError` is a **built-in Python exception type**.  
- It happens when a function receives a value that is **not valid for its operation**.  

