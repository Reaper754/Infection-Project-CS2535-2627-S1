# How To Speed Up a Simulation in Pygame

### The basic parts

Frame rate controls how often the window redraws. Simulation speed controls how much simulated time passes in each frame. Multiply delta by the speed multiplier to advance simulation time faster. Apply the same multiplier to movement and day tracking. Keep the existing frame-rate limit.

F toggles between normal and four-times speed. Scale the elapsed time while keeping the same frame rate. For collision checks, spend accumulated simulation time in small updates.

Create one object before the frame loop so its attributes persist between calls.

```python
class Simulation:
    def __init__(self) -> None:
        """Set the starting values for this simulation."""
        self.fast = False
        self.seconds = 0.0

simulation = Simulation()

def run_sim():
    # Change speed on a key press so holding F does not toggle every frame.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                simulation.fast = not simulation.fast
    if simulation.fast:
        multiplier = 4
    else:
        multiplier = 1
    # Convert frame time to seconds before applying the speed multiplier.
    delta = clock.get_time() / 1000
    simulation.seconds += delta * multiplier
    pygame.display.set_caption(f"{simulation.seconds:.1f} seconds")
```

**Documentation:** [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock) · [Keyboard events](https://pyga.me/docs/ref/event.html)
