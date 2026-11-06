import pygame
import random

# Prepare Pygame and create the drawing surface.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Project")
clock = pygame.time.Clock()
running = True

#display population
radius = 6
colours = {"susceptible": (70, 150, 240), "infected": (240, 80, 80),
           "recovered": (80, 200, 120), "dead": (150, 150, 150)}
population = []
for _ in range(50):
    velocity = pygame.Vector2(60, 0).rotate(random.uniform(0, 360))
    population.append({
        "x": random.randint(radius, screen.get_width() - radius),
        "y": random.randint(radius, screen.get_height() - radius),
        "x_speed": velocity.x, "y_speed": velocity.y,
        "status": "susceptible", "immune": False,
    })

#moving the circles
position = pygame.Vector2(400, 300)
velocity = pygame.Vector2(180, 120)
radius = 20

#day timer
SECONDS_PER_DAY = 5.0
calendar = {"day": 0, "elapsed_seconds": 0.0}

#day text
font = pygame.font.Font(None, 28)
day = 1
counts = {"susceptible": 70, "infected": 20, "recovered": 8, "dead": 2}

def run_sim():
    """Handle simulation input and draw the current frame."""
    seconds = clock.get_time() / 1000
    for person in population:
        if person["status"] != "dead":
            person["x"] += person["x_speed"] * seconds
            person["y"] += person["y_speed"] * seconds
        colour = colours[person["status"]]
        pygame.draw.circle(screen, colour, (person["x"], person["y"]), radius)
    #moving the circles around
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

    #distance between circles
    first_centre = pygame.Vector2(300, 300)
    second_centre = pygame.Vector2(pygame.mouse.get_pos())
    first_radius = 25
    second_radius = 35
    distance_limit = 50

    # Convert center distance into the gap between the edges.
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

    #day timer
    seconds = clock.get_time() / 1000
    calendar["elapsed_seconds"] += seconds

    # Process every complete day and preserve the leftover time.
    while calendar["elapsed_seconds"] >= SECONDS_PER_DAY:
        calendar["elapsed_seconds"] -= SECONDS_PER_DAY
        calendar["day"] += 1
        print(f"Day {calendar['day']} completed")
        # Record counts or apply daily simulation rules here.

    #day count
    pygame.display.set_caption(f"Simulation day: {calendar['day']}")

    lines = [f"Day: {day}"]
    for status, count in counts.items():
        lines.append(f"{status.capitalize()}: {count}")

    # Render each line, then copy it onto the window.
    y = 10
    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        screen.blit(text_surface, (10, y))
        y += 30

while running:
    # Handle the window's events each frame.
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    # Clear the old frame, then draw the new one.
    screen.fill((30, 30, 40))
    run_sim()
    pygame.display.flip()
    clock.tick(60)  # Limit the loop to 60 frames per second.

pygame.quit()