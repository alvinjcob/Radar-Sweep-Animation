import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Radar Sweep with Targets - Bresenham Algorithm")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)

center_x = WIDTH // 2
center_y = HEIGHT // 2
radius = 250

clock = pygame.time.Clock()


# -------------------------------------------------
# Bresenham Line Algorithm
# -------------------------------------------------
def bresenham_line(x1, y1, x2, y2, surface, color):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    err = dx - dy

    while True:
        surface.set_at((x1, y1), color)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy


# -------------------------------------------------
# Draw radar background
# -------------------------------------------------
def draw_radar():

    pygame.draw.circle(screen, DARK_GREEN, (center_x, center_y), radius, 1)
    pygame.draw.circle(screen, DARK_GREEN, (center_x, center_y), radius//2, 1)
    pygame.draw.circle(screen, DARK_GREEN, (center_x, center_y), radius//4, 1)

    pygame.draw.line(screen, DARK_GREEN, (center_x-radius, center_y), (center_x+radius, center_y))
    pygame.draw.line(screen, DARK_GREEN, (center_x, center_y-radius), (center_x, center_y+radius))


# -------------------------------------------------
# Create radar targets
# -------------------------------------------------
targets = []

for i in range(8):
    angle = random.randint(0, 360)
    dist = random.randint(50, radius)

    x = center_x + dist * math.cos(math.radians(angle))
    y = center_y - dist * math.sin(math.radians(angle))

    targets.append({
        "x": int(x),
        "y": int(y),
        "angle": angle,
        "visible": False,
        "timer": 0
    })


# -------------------------------------------------
# Radar sweep
# -------------------------------------------------
angle = 0
running = True

while running:

    screen.fill(BLACK)
    draw_radar()

    # Sweep endpoint
    x_end = int(center_x + radius * math.cos(math.radians(angle)))
    y_end = int(center_y - radius * math.sin(math.radians(angle)))

    # Draw sweep line using Bresenham
    bresenham_line(center_x, center_y, x_end, y_end, screen, GREEN)

    # Check targets
    for t in targets:

        if abs(angle - t["angle"]) < 2:
            t["visible"] = True
            t["timer"] = 30

        if t["visible"]:
            pygame.draw.circle(screen, GREEN, (t["x"], t["y"]), 4)
            t["timer"] -= 1

            if t["timer"] <= 0:
                t["visible"] = False


    angle += 1
    if angle >= 360:
        angle = 0

    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()