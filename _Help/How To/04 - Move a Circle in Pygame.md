# How To Move a Circle in Pygame

### The basic parts

A **position** describes where a circle's centre is. A **velocity** describes its direction and speed. `pygame.Vector2` stores an `x` and a `y` value together. Positive horizontal velocity moves right. Positive vertical velocity moves down. Negative values move in the opposite directions.

Movement is **velocity × elapsed time**. Velocity is measured in pixels per second here. `clock.get_time()` gives the milliseconds measured by the main loop's last `clock.tick()`. Dividing by `1000` converts this to seconds. This keeps movement tied to time instead of the number of frames.

A circle hits a wall when its edge reaches the window boundary. Its centre must stay at least one radius from that boundary. A bounce reverses the velocity on the affected axis. Moving the centre back inside the window prevents it from getting stuck outside.

### Example: bounce off all four walls

Position and velocity must survive between frames. These values belong outside `run_sim` so they are created once. Changing the vector's components keeps those changes for the next frame.

```python
position = pygame.Vector2(400, 300)
velocity = pygame.Vector2(180, 120)
radius = 20

def run_sim():
    seconds = clock.get_time() / 1000
    position.x += velocity.x * seconds
    position.y += velocity.y * seconds
    width, height = screen.get_size()

    # Keep the circle inside each wall and point it back inward.
    if position.x < radius:
        position.x = radius
        velocity.x = abs(velocity.x)
    elif position.x > width - radius:
        position.x = width - radius
        velocity.x = -abs(velocity.x)

    if position.y < radius:
        position.y = radius
        velocity.y = abs(velocity.y)
    elif position.y > height - radius:
        position.y = height - radius
        velocity.y = -abs(velocity.y)

    pygame.draw.circle(screen, (70, 150, 240), position, radius)
```

**Documentation:** [Vector2](https://pyga.me/docs/ref/math.html#pygame.math.Vector2) · [Clock](https://pyga.me/docs/ref/time.html#pygame.time.Clock)
