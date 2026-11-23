from random import randint

import pygame
import random
import math

from pygame.event import wait


class Simulation:
    def __init__(self) -> None:
        """Set the starting values for this simulation."""
        self.paused = False
        self.updates = 0
        self.fast = False
        self.seconds = 0.0

simulation = Simulation()

class Calendar:
    def __init__(self) -> None:
        """Set the starting values for this calendar."""
        self.day = 0
        self.seconds = 0.0

calendar = Calendar()

class Circle:
    def __init__(self, x: float, y: int, velocity_x: float, velocity_y: float, dead: bool, infected: bool, immune: bool) -> None:
        """Set the starting values for this circle."""
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.dead = dead
        self.infected = infected
        self.immune = immune

    def move(self, delta: float, width: int, radius: int, height: int) -> None:
        if self.dead:
            self.velocity_x = 0
            self.velocity_y = 0
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

population = 50

sick = random.randint(0, population)
immune = random.randint(0, population)
if sick == immune:
    if sick == 50:
        sick -= 1
    else:
        sick += 1

touching = set()
close = set()
dead = set()

circles = []
for index in range(population):
    if index == sick:
        circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False, True, False)
    elif index == immune:
        circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False, False, True)
    else:
        circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False, False, False)
    circles.append(circle)

def run_sim():
    # Handle a press once when its event arrives.
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                simulation.fast = not simulation.fast
            if event.key == pygame.K_SPACE:
                simulation.paused = not simulation.paused
                print("paused")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print(event.pos)
        # Advance the simulation only while it is running.
    if not simulation.paused:
        if simulation.fast:
            multiplier = 4
        else:
            multiplier = 1
        simulation.updates += 1
        # Check whether a key is still held this frame.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pygame.draw.circle(screen, "white", (40, 60), 10)
        """Handle simulation input and draw the current frame."""
        touching.clear()
        close.clear()
        # Move the circles before measuring the current distances.
        delta = clock.get_time() / 1000
        simulation.seconds += delta * multiplier
        calendar.seconds += delta
        # Count every completed day and carry over the unused time.
        while calendar.seconds >= 5:
            calendar.seconds -= 5
            calendar.day += 1
        # pygame.display.set_caption(f"Day {calendar.day}")
        # Render the text as a surface before copying it to the screen.
        label = font.render(f"Day {calendar.day}", True, "white")
        screen.blit(label, (10, 10))
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
                    if first_circle.infected == True or second_circle.infected == True:
                        touching.add(first_circle)
                        touching.add(second_circle)
                if first_circle.distance_to(second_circle) <= 50:
                    if first_circle.infected == True or second_circle.infected == True:
                        close.add(first_circle)
                        close.add(second_circle)
                distance = first_circle.distance_to(second_circle)
                distances.append(distance)
        for circle in circles:
            circle.move(delta, screen.get_width(), 10, screen.get_height())
            if circle.infected == True:
                die = random.randint(1, 1000)
                if die == 1:
                    dead.add(circle)
                    circle.dead = True
                    circle.infected = False
            if circle.dead == True:
                color = "grey"
            elif circle.immune == True:
                color = "white"
            elif circle.infected == True:
                color = "green"
            elif circle in touching:
                if circle.dead == True:
                    pass
                elif circle.immune == True:
                    pass
                else:
                    sick = random.randint(1, 10)
                    if sick == 1:
                        circle.infected = True
                        color = "green"
                    else:
                        color = "red"
            elif circle in close:
                if circle.dead == True:
                    pass
                elif circle.immune == True:
                    pass
                else:
                    sick = random.randint(1, 50)
                    if sick == 1:
                        circle.infected = True
                        color = "green"
                    else:
                        color = "yellow"
            else:
                color = "skyblue"
            pygame.draw.circle(screen, color, (circle.x, circle.y), 10)
    pygame.display.set_caption(f"Updates: {simulation.updates}")


# Prepare Pygame and create the drawing surface.
# Initialize Pygame before creating the window or using its modules.
pygame.init()
# Create the font once after Pygame is initialized.
font = pygame.font.Font(None, 28)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Infection")
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