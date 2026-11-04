# How To Display a Population in Pygame

### The basic parts

A **list of dictionaries** can store many people. Each dictionary holds one person's position, velocity, and status. A loop draws each person using their current data.

`random.randint()` chooses a whole number between two limits, including both limits. Keep starting centres at least one radius from each wall. `random.uniform()` chooses a decimal value between two limits. Choosing a random angle gives people different movement directions. A vector's `rotate()` method measures angles in degrees.

A **colour lookup dictionary** connects each status to a colour. Reading `colours[person["status"]]` selects the matching colour. Movement can depend on status too. Skipping position updates for dead people keeps them still while allowing them to remain visible.

### Example: random starting positions and directions

Create the population once after the window is created. Creating it inside `run_sim` would reset everyone every frame. The example starts everyone as susceptible. Changes to a person's status affect their colour on the next draw. Wall bouncing is covered in [Move a Circle in Pygame](04%20-%20Move%20a%20Circle%20in%20Pygame.md).

```python
import random

radius = 6
colours = {"susceptible": (70, 150, 240), "infected": (240, 80, 80),
           "recovered": (80, 200, 120), "dead": (150, 150, 150)}
population = []
for _ in range(50):
    velocity = pygame.Vector2(60, 0).rotate(random.uniform(0, 360))
    population.append({
        "x": random.randint(radius, screen.get_width() - radius),
        "y": random.randint(radius, screen.get_height() - radius),
        "x_speed": velocity.x, "y_speed": velocity.y,
        "status": "susceptible", "immune": False,
    })

def run_sim():
    seconds = clock.get_time() / 1000
    for person in population:
        if person["status"] != "dead":
            person["x"] += person["x_speed"] * seconds
            person["y"] += person["y_speed"] * seconds
        colour = colours[person["status"]]
        pygame.draw.circle(screen, colour, (person["x"], person["y"]), radius)
```

**Documentation:** [Random values](https://docs.python.org/3/library/random.html) · [Vector2.rotate](https://pyga.me/docs/ref/math.html#pygame.math.Vector2.rotate) · [Drawing circles](https://pyga.me/docs/ref/draw.html#pygame.draw.circle)
