import pygame
import random

class Circle:
    def __init__(self, x: float, y: int, velocity_x: float) -> None:
        """Set the starting values for this circle."""
        self.x = x
        self.y = y
        self.velocity_x = velocity_x

    def move(self, delta: float, width: int, radius: int) -> None:
        """Move horizontally and bounce at the walls."""
        self.x += self.velocity_x * delta
        # Limit the centre so the circle stays inside the window.
        right_wall = width - radius
        if self.x < radius:
            self.x = radius
            self.velocity_x *= -1
        elif self.x > right_wall:
            self.x = right_wall
            self.velocity_x *= -1

    def distance_to(self, other):
        pass

circles = []
for index in range(10):
    circle = Circle(random.randint(8, 792), random.randint(8, 592), 60)
    circles.append(circle)

def run_sim():
    """Handle simulation input and draw the current frame."""
    # Move the circles before measuring the current distances.
    delta = clock.get_time() / 1000
    for index in range(len(circles)):
        circle = circles[index]
        speed = 30 + index * 10
        circle.x += speed * delta
        if circle.x > 790:
            circle.x = 10
    distances = []
    # Start the inner loop one position later so each pair is measured once.
    for first_index in range(len(circles)):
        first_circle = circles[first_index]
        for second_index in range(first_index + 1, len(circles)):
            second_circle = circles[second_index]
            distance = first_circle.distance_to(second_circle)
            distances.append(distance)
    for circle in circles:
        pygame.draw.circle(screen, "skyblue", circle, 10)
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