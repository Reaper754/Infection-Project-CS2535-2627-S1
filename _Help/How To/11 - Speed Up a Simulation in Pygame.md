# How To Speed Up a Simulation in Pygame

### The basic parts

**Frame rate** controls how often pictures are drawn. **Simulation speed** controls how much simulated time passes. Fast-forward should advance the simulation further while keeping the window responsive.

A **speed multiplier** converts real seconds into simulation seconds. A multiplier of `1` is normal speed. A multiplier of `4` advances four simulation seconds per real second. Apply this time to movement and day tracking so both speed up together.

Small **time steps** keep updates consistent. An accumulator stores simulation time until there is enough for another step. Fast-forward runs more steps before drawing the next frame. Collision and disease checks belong inside those steps. Drawing belongs outside them.

### Example: press F to toggle four-times speed

Create the settings dictionary once outside the function. This example tracks days using the same five-second day length as the day-cycle guide. Each update advances time by `1 / 60` of a simulation second. The caption shows the speed and completed days.

```python
STEP_SECONDS = 1 / 60
SECONDS_PER_DAY = 5.0
simulation = {"speed": 1, "pending": 0.0, "day_time": 0.0, "day": 0}

def run_sim():
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f:
            simulation["speed"] = 4 if simulation["speed"] == 1 else 1

    real_seconds = clock.get_time() / 1000
    simulation["pending"] += real_seconds * simulation["speed"]

    # Advance in small steps, including during fast-forward.
    while simulation["pending"] >= STEP_SECONDS:
        simulation["pending"] -= STEP_SECONDS
        # Move people using velocity * STEP_SECONDS here.
        # Check walls, proximity, and disease rules here.
        simulation["day_time"] += STEP_SECONDS
        while simulation["day_time"] >= SECONDS_PER_DAY:
            simulation["day_time"] -= SECONDS_PER_DAY
            simulation["day"] += 1

    # Draw people here, after all simulation updates.
    pygame.display.set_caption(
        f"Day {simulation['day']} | Speed: {simulation['speed']}x"
    )
```

**Documentation:** [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock) · [Keyboard events](https://pyga.me/docs/ref/event.html)
