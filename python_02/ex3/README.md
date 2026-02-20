The `finally` block is part of exception handling and **always executes**, whether an error occurs or not.  
It does not clean anything automatically, but it is used to place **cleanup code** (such as closing a system or releasing resources).

- `try` → code that may cause an error  
- `except` → handles the error if it happens  
- `finally` → runs in all cases (with or without error)

The goal of this exercise is to understand that important code (like closing the watering system) must always run, even when an error occurs.
