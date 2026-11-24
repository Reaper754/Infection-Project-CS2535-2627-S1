import pygame
import random
import math
import matplotlib.pyplot as plt
import csv

days = []
populations = []
sicks = []
deads = []
healeds = []
healthys = []
# Open the sample using the column names from its header.
with open("data.csv", newline="", encoding="utf-8") as file:
    # Convert both values before adding them to the graph data.
    for row in csv.DictReader(file):
        days.append(int(row["day"]))
        populations.append(int(row["population"]))
        sicks.append(int(row["sick"]))
        deads.append(int(row["dead"]))
        healeds.append(int(row["healed"]))
        healthys.append(int(row["healthy"]))

plt.plot(sicks)
plt.plot(deads)
plt.plot(healeds)
plt.plot(healthys)
plt.xlabel("Day")
plt.ylabel("Population")
plt.show()

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
    def __init__(self, x: float, y: int, velocity_x: float, velocity_y: float, dead: bool, infected: bool, immune: bool, recovered: bool) -> None:
        """Set the starting values for this circle."""
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.dead = dead
        self.infected = infected
        self.immune = immune
        self.recovered = recovered

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

population = int(input("How big is the population:"))

touching = set()
close = set()
dead = set()
unhealthy = set()
healed = set()
healthy = set()
total = population

circles = []
for index in range(population):
    sick = random.random()
    immune = random.random()
    if sick < 0.05:
        circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False, True, False, False)
    elif immune < 0.05:
        circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False, False, True, False)
    else:
        circle = Circle(random.randint(8, 792), random.randint(8, 592), random.randint(-60, 60), random.randint(-60, 60), False, False, False, False)
    circles.append(circle)

def run_sim():
    # Handle a press once when its event arrives.
    for event in events:
        # Use the same flag that controls the main loop.
        global running
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                simulation.fast = not simulation.fast
                print("fast")
            if event.key == pygame.K_SPACE:
                simulation.paused = not simulation.paused
                print("paused")
            if event.key == pygame.K_q:
                running = False
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
        calendar.seconds += delta * multiplier
        pygame.display.set_caption(f"{simulation.seconds:.1f} seconds")
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
            circle.x += speed * delta * multiplier
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
                die = random.random()
                recover = random.random()
                if die < 0.001:
                    dead.add(circle)
                    circle.dead = True
                    circle.infected = False
                if recover < 0.001 and circle.infected == True:
                    circle.infected = False
                    circle.recovered = True
                    healed.add(circle)
            if circle.dead == True:
                color = "grey"
            elif circle.immune == True:
                color = "white"
            elif circle.recovered == True:
                color = "blue"
            elif circle.infected == True:
                color = "green"
            elif circle in touching:
                if circle.dead == True:
                    pass
                elif circle.immune == True:
                    pass
                elif circle.recovered == True:
                    pass
                else:
                    sick = random.random()
                    if sick < 1:
                        circle.infected = True
                        color = "green"
                        unhealthy.add(circle)
                    else:
                        color = "red"
            elif circle in close:
                if circle.dead == True:
                    pass
                elif circle.immune == True:
                    pass
                elif circle.recovered == True:
                    pass
                else:
                    sick = random.random()
                    if sick < 0.50:
                        circle.infected = True
                        color = "green"
                        unhealthy.add(circle)
                    else:
                        color = "yellow"
            else:
                color = "skyblue"
                healthy.add(circle)
            pygame.draw.circle(screen, color, (circle.x, circle.y), 10)

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