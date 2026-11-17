# How To Add Keyboard Inputs

Pygame can respond to a key being pressed or a key being held. These are useful for different actions. Click the Pygame window to give it keyboard focus before testing input.

### The basic parts

**Events** describe changes. `pygame.KEYDOWN` means a key was pressed. `pygame.KEYUP` means a key was released. `event.key` identifies the key. Pygame names keys with constants such as `pygame.K_SPACE` and `pygame.K_LEFT`. Key events suit actions such as pausing or jumping.

**Key state** describes what is held right now. `pygame.key.get_pressed()` returns the current state of the keys. `keys[pygame.K_LEFT]` is `True` while the left arrow is held. This suits continuous actions such as movement. Check held keys after the event loop so movement continues even when no new events arrive.

### Example. Detect a press or a held key

Space prints a message when pressed. Holding Left draws a marker each frame.

```python
def run_sim():
    # Handle a press once when its event arrives.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space pressed")
    # Check whether a key is still held this frame.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pygame.draw.circle(screen, "white", (40, 60), 10)
```

**Documentation:** [Keyboard states and key names](https://pyga.me/docs/ref/key.html) · [Keyboard events](https://pyga.me/docs/ref/event.html)

### Common keyboard keys

| Key | Pygame constant | Key | Pygame constant | Key | Pygame constant |
| --- | --- | --- | --- | --- | --- |
| A | `pygame.K_a` | B | `pygame.K_b` | C | `pygame.K_c` |
| D | `pygame.K_d` | E | `pygame.K_e` | F | `pygame.K_f` |
| G | `pygame.K_g` | H | `pygame.K_h` | I | `pygame.K_i` |
| J | `pygame.K_j` | K | `pygame.K_k` | L | `pygame.K_l` |
| M | `pygame.K_m` | N | `pygame.K_n` | O | `pygame.K_o` |
| P | `pygame.K_p` | Q | `pygame.K_q` | R | `pygame.K_r` |
| S | `pygame.K_s` | T | `pygame.K_t` | U | `pygame.K_u` |
| V | `pygame.K_v` | W | `pygame.K_w` | X | `pygame.K_x` |
| Y | `pygame.K_y` | Z | `pygame.K_z` | 0 | `pygame.K_0` |
| 1 | `pygame.K_1` | 2 | `pygame.K_2` | 3 | `pygame.K_3` |
| 4 | `pygame.K_4` | 5 | `pygame.K_5` | 6 | `pygame.K_6` |
| 7 | `pygame.K_7` | 8 | `pygame.K_8` | 9 | `pygame.K_9` |
| F1 | `pygame.K_F1` | F2 | `pygame.K_F2` | F3 | `pygame.K_F3` |
| F4 | `pygame.K_F4` | F5 | `pygame.K_F5` | F6 | `pygame.K_F6` |
| F7 | `pygame.K_F7` | F8 | `pygame.K_F8` | F9 | `pygame.K_F9` |
| F10 | `pygame.K_F10` | F11 | `pygame.K_F11` | F12 | `pygame.K_F12` |
| Space | `pygame.K_SPACE` | Enter | `pygame.K_RETURN` | Escape | `pygame.K_ESCAPE` |
| Tab | `pygame.K_TAB` | Backspace | `pygame.K_BACKSPACE` | Delete | `pygame.K_DELETE` |
| Left arrow | `pygame.K_LEFT` | Right arrow | `pygame.K_RIGHT` | Up arrow | `pygame.K_UP` |
| Down arrow | `pygame.K_DOWN` | Left Shift | `pygame.K_LSHIFT` | Right Shift | `pygame.K_RSHIFT` |
| Left Ctrl | `pygame.K_LCTRL` | Right Ctrl | `pygame.K_RCTRL` | Left Alt | `pygame.K_LALT` |
| Right Alt | `pygame.K_RALT` | Home | `pygame.K_HOME` | End | `pygame.K_END` |
| Page Up | `pygame.K_PAGEUP` | Page Down | `pygame.K_PAGEDOWN` | | |
