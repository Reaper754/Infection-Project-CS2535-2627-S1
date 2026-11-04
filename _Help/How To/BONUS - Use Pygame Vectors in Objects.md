# How To Use Pygame Vectors in Objects

### The basic parts

`pygame.Vector2` is a predefined class. Its objects store two numbers. A position vector stores coordinates. A velocity vector stores movement per second. Multiplying velocity by elapsed seconds gives the change in position.

A student-defined object can store vectors as **instance attributes**. `self.position` belongs to the current object. Constructing the vectors inside `__init__` gives each instance its own vectors. Constructing a vector from another vector makes a copy. Changing that copy does not change the original.

A **method** is a function attached to a class. `self` refers to the instance receiving the method call. Other objects can own a movement component and call its methods. This lets movement code stay together in one class.

### Example: a reusable movement component

The component below stores position and velocity between frames. Its `move()` method updates both coordinates together. The example draws the circle at the component's current position. The [wall-bounce guide](04%20-%20Move%20a%20Circle%20in%20Pygame.md) shows the boundary checks that can be added as another component method.

```python
class Movement:
    """Store a position and velocity for one moving object."""

    def __init__(self, position: pygame.Vector2,
                 velocity: pygame.Vector2) -> None:
        """Create independent vectors for this component."""
        self.position = pygame.Vector2(position)
        self.velocity = pygame.Vector2(velocity)

    def move(self, seconds: float) -> None:
        """Advance the position by the given elapsed time."""
        self.position += self.velocity * seconds


movement = Movement(pygame.Vector2(100, 300), pygame.Vector2(60, 0))

def run_sim():
    seconds = clock.get_time() / 1000
    movement.move(seconds)
    pygame.draw.circle(screen, (70, 150, 240), movement.position, 20)
```

**Documentation:** [Vector2](https://pyga.me/docs/ref/math.html#pygame.math.Vector2) · [Python classes](https://docs.python.org/3/tutorial/classes.html)
