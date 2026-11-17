# How To Add Mouse Inputs

Pygame can read the mouse position, button clicks, held buttons, and wheel movement. **Events** describe a change. **Mouse state** describes what is happening right now.

### The basic parts

`pygame.MOUSEBUTTONDOWN` means a button was pressed. `pygame.MOUSEBUTTONUP` means it was released. `event.button` identifies the button: `1` is left, `2` is middle, and `3` is right. `event.pos` gives the mouse position when that event happened. Use a click event for an action that should happen once per press.

`pygame.mouse.get_pos()` gives the current `(x, y)` position relative to the window's top-left corner. Increasing `x` moves right. Increasing `y` moves down. `pygame.mouse.get_pressed()` gives the held button states. Its first three positions are left, middle, and right. The left button is at index `0`, even though its event number is `1`.

### Example. Read the location of a click

The left button has event number 1. The event reports where the pointer was when the button was pressed.

```python
def run_sim():
    for event in events:
        # Check the event type before reading mouse-specific attributes.
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
```

**Documentation:** [Mouse position and button states](https://pyga.me/docs/ref/mouse.html) · [Mouse events and their attributes](https://pyga.me/docs/ref/event.html)

### Common mouse events

| Action | Event type | Useful event attributes |
| --- | --- | --- |
| Move the pointer | pygame.MOUSEMOTION | pos, rel, buttons |
| Press a mouse button | pygame.MOUSEBUTTONDOWN | pos, button |
| Release a mouse button | pygame.MOUSEBUTTONUP | pos, button |
| Scroll the wheel | pygame.MOUSEWHEEL | x, y |
