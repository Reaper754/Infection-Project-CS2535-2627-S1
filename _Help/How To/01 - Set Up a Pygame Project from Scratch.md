# How To Set Up a Pygame Project from Scratch

Pygame is a Python library for graphics, sound, and user input. **pygame-ce** is the Community Edition of Pygame. Install it by running this command in your project's terminal:

```sh
pip install pygame-ce
```

The package is called `pygame-ce`, but Python code uses `import pygame`.

### The basic parts

A Pygame program starts by **initializing** Pygame with `pygame.init()`. This prepares its modules for use. A **display surface** is the area where your program draws. `pygame.display.set_mode((width, height))` creates the window and returns this surface. The dimensions are measured in pixels.

The **main loop** keeps the program running. Each pass through the loop is a **frame**. **Events** are messages about things such as key presses or a request to close the window. The program checks these messages every frame so the window stays responsive. A `pygame.QUIT` event means the user has requested to close the window. Setting `running` to `False` stops the loop after the current frame.

Drawing a frame starts by clearing the previous picture with `fill()`. Colours use `(red, green, blue)` amounts from `0` to `255`. New shapes or images go after the background is cleared. `pygame.display.flip()` shows the finished frame in the window. A **clock** limits how often the loop repeats. `pygame.quit()` closes Pygame after the loop ends.

`run_sim` is our function for the simulation's input and drawing code. The main loop calls it once per frame. `screen` is the drawing surface created by the program. `events` is the list of messages collected for the current frame. The loop reads events once so both the close-button check and `run_sim` can use the same messages. Later examples show code to put inside this function.

### Basic example

This could be saved as `main.py`. Running it displays a blank window with a working close button.

```python
import pygame

def run_sim():
    """Handle simulation input and draw the current frame."""
    pass

# Prepare Pygame and create the drawing surface.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Project")
clock = pygame.time.Clock()
running = True

while running:
    # Handle the window's events each frame.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Clear the old frame, then draw the new one.
    screen.fill((30, 30, 40))
    run_sim()
    pygame.display.flip()
    clock.tick(60)  # Limit the loop to 60 frames per second.

pygame.quit()
```

**Documentation:** [Installation](https://github.com/pygame-community/pygame-ce/wiki/Installing-pygame%E2%80%90ce) · [Display](https://pyga.me/docs/ref/display.html) · [Events](https://pyga.me/docs/ref/event.html) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
