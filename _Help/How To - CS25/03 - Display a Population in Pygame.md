# How To Display a Population in Pygame

### The basic parts

Pygame uses pixels for positions. The top-left corner is (0, 0). The x-coordinate grows to the right. The y-coordinate grows downward. Pass the person's coordinates as a pair to pygame.draw.circle(). Create the population before the frame loop so its positions persist. Draw each person again after the screen is cleared.

A person dictionary can store position, speed, health status, and immunity. Functions can use those values to move or draw a person. These examples use only x, y, and speed.

### Draw one person

The centre comes from the person’s position. Speed is available for movement later.

```python
# Store the position and speed outside the loop so they persist.
person = {"x": 60, "y": 80, "speed": 60}

def run_sim():
    pygame.draw.circle(screen, "skyblue", (person["x"], person["y"]), 8)
```

### Create ten people

Each call to randint picks a coordinate. With an 8-pixel radius, the limits keep the circles inside the starter window.

```python
import random


people = []
# Choose new coordinates for every person.
for index in range(10):
    # Store the position and speed outside the loop so they persist.
    person = {"x": random.randint(8, 792), "y": random.randint(8, 592), "speed": 60}
    people.append(person)
```

**Documentation:** [Random values](https://docs.python.org/3/library/random.html) · [Vector2.rotate](https://pyga.me/docs/ref/math.html#pygame.math.Vector2.rotate) · [Drawing circles](https://pyga.me/docs/ref/draw.html#pygame.draw.circle)
