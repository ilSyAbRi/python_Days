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
