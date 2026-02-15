# 🌱 Exercise 1: Garden Data Organizer

## Overview
In this exercise, we learned how to **organize plant data using Object-Oriented Programming (OOP)**.  
We created a **Plant class** to store information for multiple plants instead of using separate variables.  

---

## What We Learned

- **Classes & Objects**: A class is a blueprint (`Plant`), and objects are instances of that class (`rose`, `sunflower`, `cactus`).  
- **Attributes**: Each plant has its own `name`, `height`, and `age`, stored in the object.  
- **Methods**: Functions inside a class like `get_info()` that can use `self` (or `box`) to access the object’s attributes.  
- **self / box**: Refers to the object itself. Using it inside methods lets each object work with **its own data**.  
- **Docstrings**: Triple-quoted strings inside classes and methods explain what they do. Can be accessed with `.__doc__` or shown using `help()`.  
- **Reusability**: Creating new plants is easy — just make new objects without rewriting code.  
- **Data Organization**: Using classes keeps all plant data together, making code **clean, structured, and maintainable**.  
- **Practical Python skills**: Learned to create objects, access attributes, call methods, and print formatted output.
- **`__init__` (Constructor method)**:  
  The `__init__` method runs automatically when a new object is created from the class.  
  It is used to give the object its starting data, such as `name`, `height`, and `age`.

  In other words, `__init__` prepares the object so it is ready to be used immediately after creation.

  Example:
  ```python
  def __init__(self, name, height, age):
      self.name = name
      self.height = height
      self.age = age
```


---


## File
- `ft_garden_data.py` – contains the `Plant` class and example plant objects.

 ---

## Example Usage
```python
rose = Plant("Rose", 25, 30)
sunflower = Plant("Sunflower", 80, 45)

print(rose.get_info())
print(sunflower.get_info())

# Access docstrings
print(Plant.__doc__)
print(Plant.get_info.__doc__)

# Use help() to see full info
help(Plant)
```

## Example Output
```
=== Garden Plant Registry ===
Rose: 25cm, 30 days old
Sunflower: 80cm, 45 days old
Cactus: 15cm, 120 days old

# Docstring output
A plant with name, height, and age.
Return plant info as a string.
```
