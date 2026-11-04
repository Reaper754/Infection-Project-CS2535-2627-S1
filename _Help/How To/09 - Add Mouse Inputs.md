# How To Add Mouse Inputs

Pygame can read the mouse position, button clicks, held buttons, and wheel movement. **Events** describe a change. **Mouse state** describes what is happening right now.

### The basic parts

`pygame.MOUSEBUTTONDOWN` means a button was pressed. `pygame.MOUSEBUTTONUP` means it was released. `event.button` identifies the button: `1` is left, `2` is middle, and `3` is right. `event.pos` gives the mouse position when that event happened. Use a click event for an action that should happen once per press.

`pygame.mouse.get_pos()` gives the current `(x, y)` position relative to the window's top-left corner. Increasing `x` moves right. Increasing `y` moves down. `pygame.mouse.get_pressed()` gives the held button states. Its first three positions are left, middle, and right. The left button is at index `0`, even though its event number is `1`.

### Example: follow the pointer, respond to clicks

The circle follows the pointer. It turns orange while the left button is held. Each left click prints its position in the terminal. `pygame.MOUSEMOTION` events describe movement. `pygame.MOUSEWHEEL` events provide scroll amounts in `event.x` and `event.y`.

```python
def run_sim():
    # Respond to each left click at its original position.
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(f"Clicked at {event.pos}")

    # Read held buttons after processing events.
    buttons = pygame.mouse.get_pressed()
    centre = pygame.mouse.get_pos()
    colour = (70, 150, 240)
    if buttons[0]:
        colour = (240, 150, 70)

    pygame.draw.circle(screen, colour, centre, 20)
```

**Documentation:** [Mouse position and button states](https://pyga.me/docs/ref/mouse.html) · [Mouse events and their attributes](https://pyga.me/docs/ref/event.html)
