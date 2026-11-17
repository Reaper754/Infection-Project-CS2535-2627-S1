# How To Move a Circle in Pygame

### The basic parts

Velocity is the number of pixels a circle moves per second. Its sign controls the direction. Delta is the time between frames in seconds. The clock reports milliseconds, so divide by 1000. The circle touches a wall when its edge reaches the boundary. Use its radius to find how far its centre can travel.

These examples move circles horizontally. Multiply velocity by elapsed seconds to get the change in position. At a wall, clamp the centre to the edge limit and reverse the velocity. In your project, apply the same idea to y for vertical bounces.

### Bounce one circle

```python
class Circle:
    def __init__(self, x: float, y: int, velocity_x: float) -> None:
        """Set the starting values for this circle."""
        self.x = x
        self.y = y
        self.velocity_x = velocity_x

    def move(self, delta: float, width: int, radius: int) -> None:
        """Move horizontally and bounce at the walls."""
        self.x += self.velocity_x * delta
        # Limit the centre so the circle stays inside the window.
        right_wall = width - radius
        if self.x < radius:
            self.x = radius
            self.velocity_x *= -1
        elif self.x > right_wall:
            self.x = right_wall
            self.velocity_x *= -1

circle = Circle(50, 60, 120)

def run_sim():
    # Convert the time since the previous frame to seconds.
    delta = clock.get_time() / 1000
    circle.move(delta, screen.get_width(), 10)
    pygame.draw.circle(screen, "skyblue", (circle.x, circle.y), 10)
```

### Bounce five circles

Keep the definition above. Replace the single-circle setup and run_sim with this version. Each circle keeps its own position and velocity.

```python
circles = []
for index in range(5):
    circle = Circle(50, 60 + index * 30, 80 + index * 20)
    circles.append(circle)

def run_sim():
    # Convert the time since the previous frame to seconds.
    delta = clock.get_time() / 1000
    # Update and draw each circle using its own position and velocity.
    for circle in circles:
        circle.move(delta, screen.get_width(), 10)
        pygame.draw.circle(screen, "skyblue", (circle.x, circle.y), 10)
```

**Documentation:** [Vector2](https://pyga.me/docs/ref/math.html#pygame.math.Vector2) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
