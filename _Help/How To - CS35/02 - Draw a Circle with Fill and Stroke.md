# How To Draw a Circle with Fill and Stroke

Pygame draws circles onto a **surface**. In the [project setup example](01%20-%20Set%20Up%20a%20Pygame%20Project%20from%20Scratch.md), that surface is called `screen`. Drawing happens after the background is cleared and before the finished frame is shown.

### The basic parts

A circle's **centre** is an `(x, y)` position in pixels. The window's top-left corner is `(0, 0)`. Increasing `x` moves right. Increasing `y` moves down. The **radius** is the distance from the centre to the edge.

The **fill** is the colour inside a shape. The **stroke** is its outline. `pygame.draw.circle(surface, colour, centre, radius, width)` draws either a fill or an outline. A `width` of `0` fills the circle. A positive `width` draws an outline of that thickness in pixels. The outline grows inward from the circle's edge.

A circle with both needs two drawing calls. Draw the fill first. Draw the stroke over it using the same centre and radius. Colours use `(red, green, blue)` values from `0` to `255`.

### Example 1. Draw one circle

Draw the fill first. Then draw a 3-pixel outline on top.

```python
def run_sim():
    # Draw on the display surface using a centre and a radius.
    pygame.draw.circle(screen, "skyblue", (80, 60), 15)
    # A positive width draws only the outline over the fill.
    pygame.draw.circle(screen, "white", (80, 60), 15, width=3)
```

### Example 2. Draw ten circles in a row

The x-coordinate increases by 30 pixels each time. The y-coordinate stays the same.

```python
def run_sim():
    # Keep the same y position and space the centres across the window.
    for index in range(10):
        # Draw on the display surface using a centre and a radius.
        pygame.draw.circle(screen, "skyblue", (30 + index * 30, 60), 10)
```

**Documentation:** [pygame.draw.circle](https://pyga.me/docs/ref/draw.html#pygame.draw.circle)
