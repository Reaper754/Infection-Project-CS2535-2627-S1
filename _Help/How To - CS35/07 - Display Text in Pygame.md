# How To Display Text in Pygame

### The basic parts

A **font** controls how text looks. `pygame.font.Font(None, 28)` uses Pygame's built-in font at size 28. Create the font once after `pygame.init()`.

`font.render()` turns a string into a small surface containing the text. Its second argument enables smooth letter edges. Its third argument sets the text colour. `screen.blit()` copies that surface onto the window. The position gives the text surface's top-left corner in pixels.

Text must be drawn again after the background is cleared each frame. Render changing values again to show their latest contents. Draw text after people or other shapes so those shapes do not cover it.

### Example. Draw one label

Create the font after pygame.init(). The label starts 10 pixels from the top and left edges.

```python
# Create the font once after Pygame is initialized.
font = pygame.font.Font(None, 28)

def run_sim():
    # Render the text as a surface before copying it to the screen.
    label = font.render("Day: 3", True, "white")
    screen.blit(label, (10, 10))
```

**Documentation:** [Fonts and rendering](https://pyga.me/docs/ref/font.html) · [Surface.blit](https://pyga.me/docs/ref/surface.html#pygame.Surface.blit)
