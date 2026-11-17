# How To Get the Distance Between Two Circles in Pygame

### The basic parts

Pygame's Vector2 holds an x and y coordinate. Call distance_to() on one centre and pass it the other centre. The result is in pixels. In your simulation, compare the result with your chosen proximity threshold after moving the population.

A centre is an (x, y) point. Vector2.distance_to measures the straight-line distance between two centres in pixels. The radius is only used to draw the circles. These examples show the result in the window caption.

### Two randomly placed circles

Choose starting coordinates once before the loop.

```python
import random

centres = []
# Create the starting positions once before the frame loop.
for index in range(2):
    centre = pygame.Vector2(random.randint(10, 790), random.randint(10, 590))
    centres.append(centre)

def run_sim():
    # Measure between the centres, in pixels.
    distance = centres[0].distance_to(centres[1])
    for centre in centres:
        pygame.draw.circle(screen, "skyblue", centre, 10)
    pygame.display.set_caption(f"{distance:.1f} pixels")
```

### Two moving circles

Move the centres before measuring. An if statement puts each circle back on the left when it passes the right edge.

```python
import random

centres = []
# Create the starting positions once before the frame loop.
for index in range(2):
    centre = pygame.Vector2(random.randint(10, 790), random.randint(10, 590))
    centres.append(centre)

def run_sim():
    # Move the circles before measuring the current distances.
    delta = clock.get_time() / 1000
    for index in range(len(centres)):
        centre = centres[index]
        speed = 30 + index * 10
        centre.x += speed * delta
        if centre.x > 790:
            centre.x = 10
    # Measure between the centres, in pixels.
    distance = centres[0].distance_to(centres[1])
    for centre in centres:
        pygame.draw.circle(screen, "skyblue", centre, 10)
    pygame.display.set_caption(f"{distance:.1f} pixels")
```

### Ten moving circles

The inner loop starts at the next index. This skips the circle itself and visits each pair once. Ten circles make 45 pairs. The caption shows the smallest distance.

```python
import random

centres = []
# Create the starting positions once before the frame loop.
for index in range(10):
    centre = pygame.Vector2(random.randint(10, 790), random.randint(10, 590))
    centres.append(centre)

def run_sim():
    # Move the circles before measuring the current distances.
    delta = clock.get_time() / 1000
    for index in range(len(centres)):
        centre = centres[index]
        speed = 30 + index * 10
        centre.x += speed * delta
        if centre.x > 790:
            centre.x = 10
    distances = []
    # Start the inner loop one position later so each pair is measured once.
    for first_index in range(len(centres)):
        first_centre = centres[first_index]
        for second_index in range(first_index + 1, len(centres)):
            second_centre = centres[second_index]
            distance = first_centre.distance_to(second_centre)
            distances.append(distance)
    for centre in centres:
        pygame.draw.circle(screen, "skyblue", centre, 10)
    pygame.display.set_caption(f"{len(distances)} pairs. Closest: {min(distances):.1f} pixels")
```

**Documentation:** [Vector2.distance_to](https://pyga.me/docs/ref/math.html#pygame.math.Vector2.distance_to)
