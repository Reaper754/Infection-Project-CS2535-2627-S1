# How To Display a Population in Pygame

### The basic parts

Pygame uses pixels for positions. The top-left corner is (0, 0). The x-coordinate grows to the right. The y-coordinate grows downward. Pass the person's coordinates as a pair to pygame.draw.circle(). Create the population before the frame loop so its positions persist. Draw each person again after the screen is cleared.

A person will likely need position, velocity, health status, and immunity. In CS35, the movement component owns position and velocity. The person can have methods to move, draw, and calculate infection chance using the shared disease object. The small Person below stores only x, y, and speed.

### Draw one person

The centre comes from the person’s position. Speed is available for movement later.

```python
class Person:
    def __init__(self, x: int, y: int, speed: float) -> None:
        """Set the starting values for this person."""
        self.x = x
        self.y = y
        self.speed = speed

# Store the position and speed outside the loop so they persist.
person = Person(60, 80, 60)

def run_sim():
    pygame.draw.circle(screen, "skyblue", (person.x, person.y), 8)
```

### Create ten people

Each call to randint picks a coordinate. With an 8-pixel radius, the limits keep the circles inside the starter window.

```python
import random

class Person:
    def __init__(self, x: int, y: int, speed: float) -> None:
        """Set the starting values for this person."""
        self.x = x
        self.y = y
        self.speed = speed

people = []
# Choose new coordinates for every person.
for index in range(10):
    # Store the position and speed outside the loop so they persist.
    person = Person(random.randint(8, 792), random.randint(8, 592), 60)
    people.append(person)
```

**Documentation:** [Random values](https://docs.python.org/3/library/random.html) · [Vector2.rotate](https://pyga.me/docs/ref/math.html#pygame.math.Vector2.rotate) · [Drawing circles](https://pyga.me/docs/ref/draw.html#pygame.draw.circle)
