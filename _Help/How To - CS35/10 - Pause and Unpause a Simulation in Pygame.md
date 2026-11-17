# How To Pause and Unpause a Simulation in Pygame

### The basic parts

Store a pause flag before the frame loop. Use a KEYDOWN event to switch the flag on each press of Space. Keep handling events while paused so another press can resume the simulation. Skip movement and day updates while paused. Keep drawing and calling clock.tick() so the window stays responsive.

Space toggles the pause flag. Keep handling events and drawing while paused. Only the simulation update stops.

Create one object before the frame loop so its attributes persist between calls.

```python
class Simulation:
    def __init__(self) -> None:
        """Set the starting values for this simulation."""
        self.paused = False
        self.updates = 0

simulation = Simulation()

def run_sim():
    # Keep listening for Space even when updates are paused.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                simulation.paused = not simulation.paused
    # Advance the simulation only while it is running.
    if not simulation.paused:
        simulation.updates += 1
    pygame.display.set_caption(f"Updates: {simulation.updates}")
```

**Documentation:** [Keyboard events](https://pyga.me/docs/ref/event.html) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
