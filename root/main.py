import pygame
import random
import math

class Circle:
    def __init__(self, x: float, y: int, velocity_x: float, velocity_y: float, dead: bool) -> None:
        """Set the starting values for this circle."""
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.dead = dead

    def move(self, delta: float, width: int, radius: int, height: int) -> None:
        """Move horizontally and bounce at the walls."""
        self.x += self.velocity_x * delta
        self.y += self.velocity_y * delta
        # Limit the centre so the circle stays inside the window.
        right_wall = width - radius
        if self.x < radius:
            self.x = radius
            self.velocity_x *= -1
        elif self.x > right_wall:
            self.x = right_wall
            self.velocity_x *= -1
        bottom_wall  = height - radius
        if self.y < radius:
            self.y = radius
            self.velocity_y *= -1
        elif self.y > bottom_wall:
            self.y = bottom_wall
            self.velocity_y *= -1

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

touching = set()
close = set()
dead = set()

circles = []
for index in range(10):
    circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False)
    circles.append(circle)

def run_sim():
    """Handle simulation input and draw the current frame."""
    # Move the circles before measuring the current distances.
    delta = clock.get_time() / 1000
    for index in range(len(circles)):
        circle = circles[index]
        speed = circle.velocity_x
        circle.x += speed * delta
    distances = []
    # Start the inner loop one position later so each pair is measured once.
    for first_index in range(len(circles)):
        first_circle = circles[first_index]
        for second_index in range(first_index + 1, len(circles)):
            second_circle = circles[second_index]
            if first_circle.distance_to(second_circle) <= 20:
                touching.add(first_circle)
                touching.add(second_circle)
            if first_circle.distance_to(second_circle) <= 50:
                close.add(first_circle)
                close.add(second_circle)
            distance = first_circle.distance_to(second_circle)
            distances.append(distance)
    for circle in circles:
        circle.move(delta, screen.get_width(), 10, screen.get_height())
        if circle in touching:
            color = "red"
        elif circle in close:
            color = "yellow"
        else:
            color = "skyblue"
        if color == "red":
            die = random.randint(1, 1)
            if die == 1:
                dead.add(circle)
                color = "grey"
                died = Circle(circle.x, circle.y, 0, 0,True)
                circles[circle] = died
        pygame.draw.circle(screen, color, (circle.x, circle.y), 10)

    pygame.display.set_caption(f"{len(distances)} pairs. Closest: {min(distances):.1f} pixels")

# Prepare Pygame and create the drawing surface.
# Initialize Pygame before creating the window or using its modules.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Project")
clock = pygame.time.Clock()
running = True

while running:
    # Handle the window's events each frame.
    # Read the event queue once so the loop and run_sim share the same events.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Clear the old frame, then draw the new one.
    # Clear the previous frame before drawing the next one.
    screen.fill((30, 30, 40))
    run_sim()
    pygame.display.flip()
    clock.tick(60)  # Limit the loop to 60 frames per second.

pygame.quit()