# 🌱 Exercise 1 – Different Types of Problems

This exercise introduces Python exception handling using `try` and `except`.

The goal is to demonstrate how different types of runtime errors can occur and how they can be handled safely without stopping the program.

The program shows and catches the following exceptions:
- **ValueError** – raised when invalid data is given (for example, converting `"abc"` to an integer)
- **ZeroDivisionError** – raised when dividing by zero
- **FileNotFoundError** – raised when trying to open a file that does not exist
- **KeyError** – raised when accessing a missing key in a dictionary

The exercise also demonstrates how multiple exception types can be caught using a single `except` block.

Main objectives:
- Understand why Python uses different exception types
- Learn how to catch and handle each error correctly
- Ensure the program continues running after errors occur
- Practice structured error handling with `try / except`

<br>

---

### 📘 Dictionary and KeyError (Exercise 1)

A **dictionary** in Python is a built-in data structure that stores data as  
**key–value pairs**. It allows fast access to values using unique keys.

Example:
d = {"plant": "rose"}

- `plant` → key  
- `rose` → value  

Values are retrieved by referencing their key:
d["plant"]

When a program attempts to access a key that does not exist in the dictionary:
d["missing_plant"]

<br>

---

### Handling Exceptions in Python

In Python, programs can encounter errors, called **exceptions**. To prevent crashes, we use `try` and `except`:

- **`try`**: Python attempts to run the code inside this block. If an error occurs, it stops here and passes control to the `except` block.
- **`except ValueError as e`**: Catches a specific error type (`ValueError`) and gives the actual **error object** a name `e`.
- **`ValueError`**: The **class (blueprint)** of the error.
- **`e`**: The **actual exception object** that Python creates when the error occurs.
- **`print(e)`**: Shows the message stored in the error object.
- **`type(e)`**: Shows which class (blueprint) the error object was made from.

**Difference Between `=` and `as`:**

> "as is used only in an except block to give a name to the error object Python just created."

- **`=` (assignment)**: Gives a name to a class or value. Nothing happens, no error is created.  
  ```python
  e = ValueError  # e now points to the class ValueError itself
  ```
 - as (in except): Gives a name to the error object that Python just created when an exception occurs.

 ```python
 try:
    int("abc")
except ValueError as e:
    print(e) 
```

<br>

---

#### Key Points:

- Using as e allows you to inspect the error object or print its message without crashing the program.

- You can also use type(e) to check which blueprint/class was used to create the error object.

<br>
---

#### Analogy:

- ValueError = blueprint of a house

- Python raises an error → builds the house (error object)

- as e = gives a name to the house so you can look inside

- print(e) = see the contents of the house

- type(e) = see which blueprint was used to build the house
<br>
---
#### Example:

```py
try:
    int("abc")  # This will fail and create a ValueError object
except ValueError as e:
    print(ValueError)  # prints the class itself
    print(e)           # prints the error message
    print(type(e))     # prints <class 'ValueError'>
```
