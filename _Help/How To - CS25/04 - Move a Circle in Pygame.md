# How To Move a Circle in Pygame

### The basic parts

Velocity is the number of pixels a circle moves per second. Its sign controls the direction. Delta is the time between frames in seconds. The clock reports milliseconds, so divide by 1000. The circle touches a wall when its edge reaches the boundary. Use its radius to find how far its centre can travel.

These examples move circles horizontally. Multiply velocity by elapsed seconds to get the change in position. At a wall, clamp the centre to the edge limit and reverse the velocity. In your project, apply the same idea to y for vertical bounces.

### Bounce one circle

```python
def move_circle(circle, delta, width, radius):
    """Move horizontally and bounce at the walls."""
    circle["x"] += circle["velocity_x"] * delta
    # Limit the centre so the circle stays inside the window.
    right_wall = width - radius
    if circle["x"] < radius:
        circle["x"] = radius
        circle["velocity_x"] *= -1
    elif circle["x"] > right_wall:
        circle["x"] = right_wall
        circle["velocity_x"] *= -1

circle = {"x": 50, "y": 60, "velocity_x": 120}

def run_sim():
    # Convert the time since the previous frame to seconds.
    delta = clock.get_time() / 1000
    move_circle(circle, delta, screen.get_width(), 10)
    pygame.draw.circle(screen, "skyblue", (circle["x"], circle["y"]), 10)
```

### Bounce five circles

Keep the definition above. Replace the single-circle setup and run_sim with this version. Each circle keeps its own position and velocity.

```python
circles = []
for index in range(5):
    circle = {"x": 50, "y": 60 + index * 30, "velocity_x": 80 + index * 20}
    circles.append(circle)

def run_sim():
    # Convert the time since the previous frame to seconds.
    delta = clock.get_time() / 1000
    # Update and draw each circle using its own position and velocity.
    for circle in circles:
        move_circle(circle, delta, screen.get_width(), 10)
        pygame.draw.circle(screen, "skyblue", (circle["x"], circle["y"]), 10)
```

**Documentation:** [Vector2](https://pyga.me/docs/ref/math.html#pygame.math.Vector2) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
