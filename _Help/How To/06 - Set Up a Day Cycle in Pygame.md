# How To Set Up a Day Cycle in Pygame

### The basic parts

A **simulation day** is a unit of time defined by your program. It does not have to last 24 real hours. For example, 5 seconds of simulation time could represent one day.

An **accumulator** stores elapsed time between frames. `clock.get_time() / 1000` gives the seconds measured by the main loop's last `clock.tick()`. Add those seconds to the accumulator each frame. A day ends when the accumulated time reaches your chosen day length.

Subtract the day length instead of resetting the accumulator to zero. This keeps any leftover time for the next day. Use a `while` loop so every completed day is counted if one frame covers several days. This also supports fast-forwarding.

### Example: one day every five seconds

The dictionary below stores time between calls. Create it once outside the function. The simulation starts on day 0. Each completed day prints a message in the terminal. Daily actions belong inside the inner loop. These could include recording population counts or updating recovery times.

```python
SECONDS_PER_DAY = 5.0
calendar = {"day": 0, "elapsed_seconds": 0.0}

def run_sim():
    seconds = clock.get_time() / 1000
    calendar["elapsed_seconds"] += seconds

    # Process every complete day and preserve the leftover time.
    while calendar["elapsed_seconds"] >= SECONDS_PER_DAY:
        calendar["elapsed_seconds"] -= SECONDS_PER_DAY
        calendar["day"] += 1
        print(f"Day {calendar['day']} completed")
        # Record counts or apply daily simulation rules here.

    pygame.display.set_caption(f"Simulation day: {calendar['day']}")
```

**Documentation:** [Clock.get_time](https://pyga.me/docs/ref/time.html#pygame.time.Clock.get_time) · [Window caption](https://pyga.me/docs/ref/display.html#pygame.display.set_caption)
