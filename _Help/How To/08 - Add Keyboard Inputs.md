# How To Add Keyboard Inputs

Pygame can respond to a key being pressed or a key being held. These are useful for different actions. Click the Pygame window to give it keyboard focus before testing input.

### The basic parts

**Events** describe changes. `pygame.KEYDOWN` means a key was pressed. `pygame.KEYUP` means a key was released. `event.key` identifies the key. Pygame names keys with constants such as `pygame.K_SPACE` and `pygame.K_LEFT`. Key events suit actions such as pausing or jumping.

**Key state** describes what is held right now. `pygame.key.get_pressed()` returns the current state of the keys. `keys[pygame.K_LEFT]` is `True` while the left arrow is held. This suits continuous actions such as movement. Check held keys after the event loop so movement continues even when no new events arrive.

### Example: press Space, hold the left arrow

Space prints a message in the terminal when pressed. The circle stays orange while the left arrow is held. It returns to blue when the key is released. For typing text, use `pygame.TEXTINPUT` events instead of checking held keys.

```python
def run_sim():
    # Respond to a new key press.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space was pressed!")

    # Check held keys every frame, outside the event loop.
    keys = pygame.key.get_pressed()
    colour = (70, 150, 240)
    if keys[pygame.K_LEFT]:
        colour = (240, 150, 70)

    pygame.draw.circle(screen, colour, (400, 300), 20)
```

**Documentation:** [Keyboard states and key names](https://pyga.me/docs/ref/key.html) · [Keyboard events](https://pyga.me/docs/ref/event.html)
