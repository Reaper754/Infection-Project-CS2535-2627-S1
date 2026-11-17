# How To Set Up a Day Cycle in Pygame

### The basic parts

Keep a day number and a running total of elapsed simulation time. Add delta each frame. When there is enough time for a day, subtract the day length and increase the day number. Keep the leftover time. A while loop handles frames that complete more than one day. Record a daily CSV row inside that loop.

Five simulated seconds make one day. Keep the leftover time for the next day. The while loop counts every completed day.

Create one object before the frame loop so its attributes persist between calls.

```python
class Calendar:
    def __init__(self) -> None:
        """Set the starting values for this calendar."""
        self.day = 0
        self.seconds = 0.0

calendar = Calendar()

def run_sim():
    delta = clock.get_time() / 1000
    calendar.seconds += delta
    # Count every completed day and carry over the unused time.
    while calendar.seconds >= 5:
        calendar.seconds -= 5
        calendar.day += 1
    pygame.display.set_caption(f"Day {calendar.day}")
```

**Documentation:** [Clock.get_time](https://pyga.me/docs/ref/time.html#pygame.time.Clock.get_time) · [Window caption](https://pyga.me/docs/ref/display.html#pygame.display.set_caption)
