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

-> Because of this, PrizeFlower inherits everything from both its parent and grandparent.

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
