# How To Get the Distance Between Two Circles in Pygame

### The basic parts

Each circle has a centre and a radius. **Centre distance** measures the straight line between the two centres. `pygame.Vector2.distance_to()` calculates this distance in pixels. It uses both the horizontal and vertical separation.

**Edge distance** is the gap between the circles. Subtract both radii from the centre distance to get this gap. A positive gap means the circles are separate. A gap of zero means they touch. A negative gap means they overlap.

For disease transmission, a distance limit can describe how close people must be. Decide whether that limit measures between centres or between edges. Use the same meaning throughout the simulation.

### Example: highlight nearby circles

The circles turn orange when their edges are within 50 pixels. The first centre is at `(300, 300)`. The second centre follows the mouse. Touching or overlapping circles turn red. This example measures proximity without moving the circles apart. `distance_to()` handles the distance calculation.

```python
def run_sim():
    first_centre = pygame.Vector2(300, 300)
    second_centre = pygame.Vector2(pygame.mouse.get_pos())
    first_radius = 25
    second_radius = 35
    distance_limit = 50

    # Convert centre distance into the gap between the edges.
    centre_distance = first_centre.distance_to(second_centre)
    edge_distance = centre_distance - first_radius - second_radius
    touching = edge_distance <= 0
    nearby = edge_distance <= distance_limit

    colour = (70, 150, 240)
    if nearby:
        colour = (240, 150, 70)
    if touching:
        colour = (230, 70, 70)

    pygame.draw.circle(screen, colour, first_centre, first_radius)
    pygame.draw.circle(screen, colour, second_centre, second_radius)
```

**Documentation:** [Vector2.distance_to](https://pyga.me/docs/ref/math.html#pygame.math.Vector2.distance_to)
