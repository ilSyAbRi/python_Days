## Exercise 4 – Raising Your Own Errors

- In Python, all errors (exceptions) are objects that inherit from the base class `Exception`.

`ValueError` is a built-in subclass of `Exception`, used when a function receives an invalid value.

### ValueError and Error Messages (Python)

`ValueError` is an exception type (class) in Python that represents invalid values passed to a function.

`ValueError` does not have a fixed default message.  
Each time it is raised, a **new error object is created with a message**:

- Python may generate a message automatically (e.g., `int("abc")`)
- or the programmer can define a custom message using `raise ValueError("message")`

##### Example:

```python
raise ValueError("Plant name cannot be empty!")
```

The message "invalid literal for int() with base 10: 'abc'" is not a built-in default of ValueError; it is a context-specific message produced by Python when int() raises the exception.

- **`raise`** stops the function and sends an error to the caller; can be used alone.  
- **`try/except`** catches errors safely; can be anywhere in the call stack.  
- Combining `raise` + `try/except` lets you **detect problems and handle them without crashing**.  
- You can use `raise` with **any condition you consider an error**, for example:  
  - If a value is above a certain number (e.g., water level > 20)  
  - If a value is below a minimum  
  - Any custom rule your program requires  
- Example: invalid plant name, water level, or sunlight hours triggers `ValueError` and is caught in a test function.
