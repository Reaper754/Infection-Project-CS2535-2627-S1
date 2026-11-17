# How To Speed Up a Simulation in Pygame

### The basic parts

**Frame rate** controls how often pictures are drawn. **Simulation speed** controls how much simulated time passes. Fast-forward should advance the simulation further while keeping the window responsive.

A **speed multiplier** converts real seconds into simulation seconds. A multiplier of `1` is normal speed. A multiplier of `4` advances four simulation seconds per real second. Apply this time to movement and day tracking so both speed up together.

Small **time steps** keep updates consistent. An accumulator stores simulation time until there is enough for another step. Fast-forward runs more steps before drawing the next frame. Collision and disease checks belong inside those steps. Drawing belongs outside them.

### Example. Toggle the speed multiplier

Press F to switch between normal and four-times speed. This counter shows the conversion from real time to simulated time. For movement and collisions, use the accumulated time to run multiple small updates.

```python
state = {"fast": False, "seconds": 0.0}

def run_sim():
    # Change speed on a key press so holding F does not toggle every frame.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                state["fast"] = not state["fast"]
    if state["fast"]:
        speed = 4
    else:
        speed = 1
    # Convert frame time to seconds before applying the speed multiplier.
    delta = clock.get_time() / 1000
    state["seconds"] += delta * speed
```

**Documentation:** [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock) · [Keyboard events](https://pyga.me/docs/ref/event.html)
