
# 🌱 Exercise 4 – Garden Security System

**Objective:**<br>
Create a secure Python system that protects plant data from accidental corruption using classes and proper encapsulation.

---

## What This Code Does & What I Learned

- **Private variables:**<br>
  `__height` and `__age` are hidden so they cannot be modified directly from outside the class.  

- **Setters and getters:**<br>
  - `set_height()` and `set_age()` safely update values and print messages.  
  - `get_height()` and `get_age()` allow reading the private values safely.  

- **Data validation:**<br>
  Negative heights or ages are rejected with clear messages.  

- **Encapsulation:**<br>
  Practiced protecting important data while allowing controlled access.  

- **Printing & formatting:**<br>
  Learned the difference between using commas and `+ str()` in `print()`:  
  - **Commas** automatically add a space and convert numbers to strings, which is convenient.  
  - **`+ str()`** lets you control spacing and formatting manually, but you must convert numbers yourself and add spaces where needed.<br>
    Using both helped me understand how Python prints work and how to make the output look exactly like I want.  

- **Interactive mode lesson:**<br>
  Even in `python -i`, private variables cannot be accessed directly — only through getters and setters.

---

## How It Works

1. A `SecurePlant` object is created with a name.  
2. Use `set_height()` and `set_age()` to safely update plant data.  
3. Invalid inputs (negative values) are rejected with messages explaining why.  
4. `get_height()` and `get_age()` allow checking current values.  
5. The current plant data is printed in a clean, readable format at the end.  

---

## Example Output
```
=== Garden Security System ===
Plant created: Rose
Height updated: 25cm [OK]
Age updated: 30 days [OK]

Invalid operation attempted: height -5cm [REJECTED]
Security: Negative height rejected

Current plant: Rose (25cm, 30 days)
```

---

This exercise reinforced:<br>

- **Safe object-oriented programming**  
- **Data validation**  
- **Clear Python coding practices**  

It also gave practical insight into **why encapsulation matters**, even in a simple plant management system.

