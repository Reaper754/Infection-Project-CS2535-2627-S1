# How To Save and Restore Pygame Vectors with JSON

### The basic parts

JSON can store numbers, strings, Booleans, lists, and dictionaries. It cannot directly store a `pygame.Vector2` or an instance of your own class. Saving an object means converting its data into these supported types.

`list(vector)` produces a list containing its two coordinates. `pygame.Vector2(coordinates)` builds a vector from that list. Loading JSON restores the list rather than automatically recreating the vector. Your code must construct the vector again.

The same idea applies to a movement component. Save its position and velocity as data. Create a new component from that data when loading. A person's saved type can identify which class to construct. Shared objects such as the trial's disease should be restored once and passed to each reconstructed person.

### Example: convert a movement component to and from saved data

This uses the `Movement` class from [Use Pygame Vectors in Objects](BONUS%20-%20Use%20Pygame%20Vectors%20in%20Objects.md). The saved text represents the same data that `json.dump()` writes to a file. `json.loads()` reads text, while `json.load()` reads a file. Saving and loading happen in response to user actions rather than every frame.

```python
import json

def movement_to_data(movement: Movement) -> dict:
    """Convert a movement component to JSON-compatible data."""
    return {
        "position": list(movement.position),
        "velocity": list(movement.velocity),
    }

def movement_from_data(data: dict) -> Movement:
    """Rebuild a movement component from saved coordinates."""
    return Movement(
        pygame.Vector2(data["position"]),
        pygame.Vector2(data["velocity"]),
    )

original = Movement(pygame.Vector2(100, 300), pygame.Vector2(60, -20))
saved_text = json.dumps(movement_to_data(original))
loaded_data = json.loads(saved_text)
restored = movement_from_data(loaded_data)
```

**Documentation:** [Vector conversion](https://pyga.me/docs/ref/math.html#pygame.math.Vector2) · [JSON encoding and decoding](https://docs.python.org/3/library/json.html)
