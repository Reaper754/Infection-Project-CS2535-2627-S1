# How To End a Simulation in Pygame

### The basic parts

The setup guide's `running` variable controls the main loop. Setting it to `False` allows the loop to finish. The program can then close Pygame and continue to a graph or a terminal menu.

A function needs `global running` to assign a new value to that variable outside the function. Without `global`, the assignment creates a local variable instead. The main loop would continue using its original value.

A **stop condition** describes when a simulation is complete. `all()` checks whether every item passes a condition. It returns `True` for an empty collection too. Check that the population is not empty before using it to decide that everyone has reached a final status.

### Example. Stop the main loop with Q

Setting running to False lets the frame finish. After the loop, the setup code calls pygame.quit(). A completion rule can set the same flag.

```python
def run_sim():
    # Use the same flag that controls the main loop.
    global running
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
```

**Documentation:** [Pygame quit](https://pyga.me/docs/ref/pygame.html#pygame.quit) · [Keyboard events](https://pyga.me/docs/ref/event.html) · [all](https://docs.python.org/3/library/functions.html#all)
