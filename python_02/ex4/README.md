## Exercise 4 – Raising Your Own Errors

- In Python, all errors (exceptions) are objects that inherit from the base class `Exception`.

`ValueError` is a built-in subclass of `Exception`, used when a function receives an invalid value.

- **`raise`** stops the function and sends an error to the caller; can be used alone.  
- **`try/except`** catches errors safely; can be anywhere in the call stack.  
- Combining `raise` + `try/except` lets you **detect problems and handle them without crashing**.  
- You can use `raise` with **any condition you consider an error**, for example:  
  - If a value is above a certain number (e.g., water level > 20)  
  - If a value is below a minimum  
  - Any custom rule your program requires  
- Example: invalid plant name, water level, or sunlight hours triggers `ValueError` and is caught in a test function.
