# How To Pause and Unpause a Simulation in Pygame

### The basic parts

Store a pause flag before the frame loop. Use a KEYDOWN event to switch the flag on each press of Space. Keep handling events while paused so another press can resume the simulation. Skip movement and day updates while paused. Keep drawing and calling clock.tick() so the window stays responsive.

Pausing stops simulation updates. The window must still process events while paused. Otherwise it cannot respond to an unpause key or a close request. The main loop should also keep clearing and drawing the screen.

A **Boolean flag** stores whether the simulation is paused. `not` reverses a Boolean value. A Space key event can toggle the flag once per press. Check events before deciding whether to update the simulation.

Keep movement, day tracking, and disease changes inside the unpaused section. Keep drawing outside that section. Continue calling the main loop's `clock.tick()` while paused. This prevents paused time from accumulating into a large update when play resumes.

### Example. Skip an update while paused

Space toggles the flag. The counter advances only when unpaused. Event handling and drawing can continue every frame.

```python
state = {"paused": False, "updates": 0}

def run_sim():
    # Keep listening for Space even when updates are paused.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                state["paused"] = not state["paused"]
    # Advance the simulation only while it is running.
    if not state["paused"]:
        state["updates"] += 1
```

**Documentation:** [Keyboard events](https://pyga.me/docs/ref/event.html) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
