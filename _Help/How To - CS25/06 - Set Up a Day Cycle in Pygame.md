# How To Set Up a Day Cycle in Pygame

### The basic parts

A **simulation day** is a unit of time defined by your program. It does not have to last 24 real hours. For example, 5 seconds of simulation time could represent one day.

An **accumulator** stores elapsed time between frames. `clock.get_time() / 1000` gives the seconds measured by the main loop's last `clock.tick()`. Add those seconds to the accumulator each frame. A day ends when the accumulated time reaches your chosen day length.

Subtract the day length instead of resetting the accumulator to zero. This keeps any leftover time for the next day. Use a `while` loop so every completed day is counted if one frame covers several days. This also supports fast-forwarding.

### Example. Count completed days

The dictionary keeps time between frames. Each day represents five simulation seconds.

```python
calendar = {"day": 0, "seconds": 0.0}

def run_sim():
    delta = clock.get_time() / 1000
    calendar["seconds"] += delta
    # Count every completed day and carry over the unused time.
    while calendar["seconds"] >= 5:
        calendar["seconds"] -= 5
        calendar["day"] += 1
        print(calendar["day"])
```

**Documentation:** [Clock.get_time](https://pyga.me/docs/ref/time.html#pygame.time.Clock.get_time) · [Window caption](https://pyga.me/docs/ref/display.html#pygame.display.set_caption)
