# How To Pause and Unpause a Simulation in Pygame

### The basic parts

Pausing stops simulation updates. The window must still process events while paused. Otherwise it cannot respond to an unpause key or a close request. The main loop should also keep clearing and drawing the screen.

A **Boolean flag** stores whether the simulation is paused. `not` reverses a Boolean value. A Space key event can toggle the flag once per press. Check events before deciding whether to update the simulation.

Keep movement, day tracking, and disease changes inside the unpaused section. Keep drawing outside that section. Continue calling the main loop's `clock.tick()` while paused. This prevents paused time from accumulating into a large update when play resumes.

### Example: pause a moving circle with Space

The dictionary stores the pause flag and position between frames. The circle stops while paused. Its outline remains visible because drawing continues. The caption shows the current pause state.

```python
simulation = {"paused": False, "x": 100.0}

def run_sim():
    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            simulation["paused"] = not simulation["paused"]

    # Only simulation updates stop during a pause.
    if not simulation["paused"]:
        seconds = clock.get_time() / 1000
        simulation["x"] += 100 * seconds
        if simulation["x"] > screen.get_width() - 20:
            simulation["x"] = 20
        # Day tracking and disease updates also belong in this section.

    pygame.draw.circle(screen, (70, 150, 240), (simulation["x"], 300), 20)
    title = "Paused" if simulation["paused"] else "Running"
    pygame.display.set_caption(title)
```

When combined with [fast-forward](11%20-%20Speed%20Up%20a%20Simulation%20in%20Pygame.md), only add elapsed time to the simulation accumulator while unpaused. Drawing and event handling still happen every frame.

**Documentation:** [Keyboard events](https://pyga.me/docs/ref/event.html) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
