# How To End a Simulation in Pygame

### The basic parts

The setup guide's `running` variable controls the main loop. Setting it to `False` allows the loop to finish. The program can then close Pygame and continue to a graph or a terminal menu.

A function needs `global running` to assign a new value to that variable outside the function. Without `global`, the assignment creates a local variable instead. The main loop would continue using its original value.

A **stop condition** describes when a simulation is complete. `all()` checks whether every item passes a condition. It returns `True` for an empty collection too. Check that the population is not empty before using it to decide that everyone has reached a final status.

### Example: quit with Q or stop when everyone is finished

This example uses your existing `population` list. Each person's dictionary has a `status`. A mixture of dead and recovered people satisfies the condition. Any susceptible or infected person prevents automatic completion.

```python
def run_sim():
    global running

    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
            return

    # Normal simulation updates and drawing belong here.

    finished = bool(population) and all(
        person["status"] in ("dead", "recovered")
        for person in population
    )
    if finished:
        running = False
```

The main loop still finishes its current frame. `pygame.quit()` belongs after that loop. Show the results graph after the loop ends rather than inside `run_sim`. Calling `pygame.quit()` alone does not stop a Python loop.

**Documentation:** [Pygame quit](https://pyga.me/docs/ref/pygame.html#pygame.quit) · [Keyboard events](https://pyga.me/docs/ref/event.html) · [all](https://docs.python.org/3/library/functions.html#all)
