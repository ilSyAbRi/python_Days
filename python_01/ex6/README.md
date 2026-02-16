
# Garden Analytics

```
Build a comprehensive garden data analytics platform that processes and analyzes garden data.
This system needs to handle complex data relationships and provide detailed
analytics using nested components and inheritance chains.
```

---

## What is a nested class?

> A nested class is just a class defined inside another class.
```py
class GardenManager:
    
    class GardenStats:   # nested class
        def __init__(self, garden):
            self.garden = garden

```
- GardenStats only exists inside GardenManager.
- You access it like: GardenManager.GardenStats(garden1)

### Why do we use it here?

#### Think of the problem:

- Each garden has plants

- We want to calculate stats for each garden:
```
Total growth

Number of plants

Plant types
```
- We don’t want these functions floating around globally, because they belong to a garden system, not the world.

#### Nested class solves this:

- Keeps stats logic inside GardenManager → organized

- Makes clear that GardenStats only works with gardens

- Helps separate “managing gardens” vs “calculating stats”

### Types of Methods in GardenManager

#### Instance Methods

- Work on one specific garden

- Access instance variables like self.plants

> Example: add_plant(), grow_all_plants(), show_report()

- Use when you want to affect only one garden

#### Class Methods (@classmethod)

- Work on the class itself, not a single object

- Access class variables like all_gardens

> Example: total_gardens(), create_garden_network()

- Use when you want to affect or get info about all gardens

#### Static Methods (@staticmethod)

- Don’t depend on instance or class

- Useful for utility functions inside the class

> Example: validate_height()

- Use for helpers that don’t need garden data

---

##### Quick summary:

- Instance → per garden

- Class → whole system

- Static → helper functions

---


```
Plant             → name, height, grow()
   ↓
FloweringPlant   → adds flower_color, blooming_state
   ↓
PrizeFlower      → adds prize_points
```
- Plant → parent

- FloweringPlant → child of Plant

- PrizeFlower → child of FloweringPlant (grandchild of Plant)

> Because of this, PrizeFlower inherits everything from both its parent and grandparent.

## Class Variable (shared by all objects of GardenManager)

```
GardenManager Class
+---------------------+
| all_gardens = [...] |
+---------------------+

alice (instance of GardenManager)
+----------------+
| owner = Alice  |
| plants = [Rose]|
+----------------+

bob (instance of GardenManager)
+----------------+
| owner = Bob    |
| plants = [Oak] |
+----------------+

all_gardens (class variable)
[alice, bob]

```

## Diagram: Class Variable vs Instance Variable

```
            GardenManager Class
       +----------------------------+
       | all_gardens = [alice,bob] |  <-- Class Variable (shared)
       +----------------------------+
                 ↑
                 ↑ used by all instances

alice (instance of GardenManager)           bob (instance of GardenManager)
+---------------------+                     +---------------------+
| owner = "Alice"     |                     | owner = "Bob"       |
| plants = ["Rose"]   | <-- Instance var     | plants = ["Oak"]    | <-- Instance var
+---------------------+                     +---------------------+


```

## Tracking All Gardens
```
GardenManager.all_gardens.append(self)
```
- Adds the current garden object (self) to the shared class list all_gardens.

- all_gardens is a class variable that keeps track of every garden created.

- append() is a built-in Python list method that adds items to the end of a list.

- This ensures the system can access all gardens at once, for example to calculate totals, scores, or create a network.

## Build the full system

#### 1. Plant classes

- Plant → base

- FloweringPlant → adds flowers

- PrizeFlower → adds prize points

#### 2. GardenManager class

- self.plants → plants in this garden

- all_gardens → class variable, tracks all gardens

#### 3. Nested GardenStats

- Calculates analytics for a specific garden

> Example: total growth, number of plants, plant types

#### 4. Methods

- Instance → add_plant(), grow_all_plants(), show_report()

- Class → total_gardens(), create_garden_network()

- Static → validate_height()

#### 5. Output

- Add plants to gardens

- Grow plants

- Show reports

- Use class method to show total gardens

- Use static method for validation
