# How To Display Text in Pygame

### The basic parts

A **font** controls how text looks. `pygame.font.Font(None, 28)` uses Pygame's built-in font at size 28. Create the font once after `pygame.init()`.

`font.render()` turns a string into a small surface containing the text. Its second argument enables smooth letter edges. Its third argument sets the text colour. `screen.blit()` copies that surface onto the window. The position gives the text surface's top-left corner in pixels.

Text must be drawn again after the background is cleared each frame. Render changing values again to show their latest contents. Draw text after people or other shapes so those shapes do not cover it.

### Example: show a day and population counts

The sample values below stand in for your simulation's current values. The font initialization belongs after `pygame.init()` and before the main loop. The loop places each line 30 pixels below the previous line.

```python
font = pygame.font.Font(None, 28)
day = 3
counts = {"susceptible": 70, "infected": 20, "recovered": 8, "dead": 2}

def run_sim():
    lines = [f"Day: {day}"]
    for status, count in counts.items():
        lines.append(f"{status.capitalize()}: {count}")

    # Render each line, then copy it onto the window.
    y = 10
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (10, y))
        y += 30
```

**Documentation:** [Fonts and rendering](https://pyga.me/docs/ref/font.html) · [Surface.blit](https://pyga.me/docs/ref/surface.html#pygame.Surface.blit)
