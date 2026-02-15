 🌱 Exercise 5 – Specialized Plant Types

This exercise practices **Object-Oriented Programming (OOP)** in Python.  
We created a base `Plant` class with common attributes: `name`, `height`, and `age`. <br>
Then we made child classes for specialized plants: <br>

- **🌸 Flower** → adds `color` and a method `bloom()`  
- **🌲 Tree** → adds `trunk_diameter` and a method `produce_shade()`  
- **🥕 Vegetable** → adds `harvest_season` and `nutritional_value` (no extra method)  

We also created **multiple instances** of each type to see how objects store their own data. <br>
`super()` is used in children to initialize the parent attributes. <br>
Output is organized with methods like `show_info()` and f-strings. <br>
Flower and Tree have actions, Vegetable just shows info. <br>
This shows how shared traits stay in the parent while unique traits go in the children, avoiding code repetition. <br>

<br>

## 🌟 Example Output

```
=== Garden Plant Types ===

Rose (Flower): 25cm, 30 days, red color
Rose is blooming beautifully!<br>

Lily (Flower): 20cm, 25 days, white color
Lily is blooming beautifully!<br>

Oak (Tree): 500cm, 1825 days, 50cm diameter
Oak provides 75.0 square meters of shade<br>

Pine (Tree): 600cm, 2000 days, 60cm diameter
Pine provides 90.0 square meters of shade<br>

Tomato (Vegetable): 80cm, 90 days, summer harvest
Tomato is rich in vitamin C<br>

Carrot (Vegetable): 30cm, 60 days, spring harvest
Carrot is rich in vitamin A
```
