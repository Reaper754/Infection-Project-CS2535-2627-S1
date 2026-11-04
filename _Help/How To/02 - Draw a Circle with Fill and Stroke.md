# How To Draw a Circle with Fill and Stroke

Pygame draws circles onto a **surface**. In the [project setup example](01%20-%20Set%20Up%20a%20Pygame%20Project%20from%20Scratch.md), that surface is called `screen`. Drawing happens after the background is cleared and before the finished frame is shown.

### The basic parts

A circle's **centre** is an `(x, y)` position in pixels. The window's top-left corner is `(0, 0)`. Increasing `x` moves right. Increasing `y` moves down. The **radius** is the distance from the centre to the edge.

The **fill** is the colour inside a shape. The **stroke** is its outline. `pygame.draw.circle(surface, colour, centre, radius, width)` draws either a fill or an outline. A `width` of `0` fills the circle. A positive `width` draws an outline of that thickness in pixels. The outline grows inward from the circle's edge.

A circle with both needs two drawing calls. Draw the fill first. Draw the stroke over it using the same centre and radius. Colours use `(red, green, blue)` values from `0` to `255`.

### Example: a blue circle with a dark outline

For a solid circle, use only the fill call. For a hollow circle, use only the stroke call. Redraw the circle each frame because `screen.fill()` clears the previous frame.

```python
def run_sim():
    centre = (400, 300)
    radius = 50
    fill_colour = (70, 150, 240)
    stroke_colour = (20, 30, 50)
    stroke_width = 4

    # Fill first, then draw the outline over the fill.
    pygame.draw.circle(screen, fill_colour, centre, radius, width=0)
    pygame.draw.circle(screen, stroke_colour, centre, radius, width=stroke_width)
```

**Documentation:** [pygame.draw.circle](https://pyga.me/docs/ref/draw.html#pygame.draw.circle)
