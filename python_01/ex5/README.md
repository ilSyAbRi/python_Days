# 🌿 Exercise 5 – Specialized Plant Types

“I’ll leave this exercise for later.”

This exercise practices **Object-Oriented Programming (OOP)** in Python.  
It demonstrates how a base class can store shared traits while child classes handle unique features. <br>

The **base class `Plant`** contains common attributes:  
- `name`  
- `height`  
- `age` <br>

Specialized child classes add their own features:  

- **🌸 Flower**  
  - Attribute: `color`  
  - Method: `bloom()` → shows the flower blooming  

- **🌲 Tree**  
  - Attribute: `trunk_diameter`  
  - Method: `produce_shade()` → calculates and prints shade area  

- **🥕 Vegetable**  
  - Attributes: `harvest_season`, `nutritional_value`  
  - No extra method, just displays info  

- Multiple **instances** are created for each type to show how objects hold their own data. <br>
- `super()` is used in child classes to initialize the parent attributes. <br>
- Methods like `show_info()` and f-strings keep the output clean and readable. <br>
- Flower and Tree have actions, while Vegetable only shows information. <br>
- This approach demonstrates **code reuse** and avoids duplication of shared traits. <br>

---

<br>

## 💡 Learning Points

- Understanding **inheritance** and parent-child relationships  
- Using **`super()`** to initialize parent attributes in children  
- Adding **unique traits and methods** to child classes  
- Creating **multiple instances** to test OOP behavior  
- Using **methods for actions** like `bloom()` and `produce_shade()`  
- Avoiding **code duplication** for shared attributes  

---

<br>

## 📝 Notes

- Vegetables don’t have extra actions; they just show info  
- Tree’s `produce_shade()` can calculate shade dynamically using `trunk_diameter`  
- Flower’s `bloom()` is an example of an action method  
- `show_info()` methods help keep output clean and consistent  

---

<br>

## 📌 How to Run

```py
python3 ft_plant_types.py
```

## 🌟 Example Output

```py
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

