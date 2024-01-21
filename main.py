import os
import sys

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

pixel_size = 10
half_pixel_size = pixel_size // 2
edges = []
direction = "right"


def get_next_pixel():
    global x, y, direction, edges
    if direction == "right":
        x += pixel_size
        if x > edges[1]:
            direction = "down"
            edges[1] = x
    elif direction == "left":
        x -= pixel_size
        if x < edges[0]:
            direction = "up"
            edges[0] = x
    elif direction == "up":
        y -= pixel_size
        if y < edges[2]:
            direction = "right"
            edges[2] = y
    elif direction == "down":
        y += pixel_size
        if y > edges[3]:
            direction = "left"
            edges[3] = y
    return x, y


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the starting position
x = screen_width // 2
y = screen_height // 2

edges = [x, x, y, y]

# Set the color
red = (255, 0, 0)
green = (0, 255, 0)

screen.fill((0, 0, 0))
pygame.draw.rect(
    screen,
    green,
    (
        x,
        y,
        pixel_size,
        pixel_size,
    ),
)
pygame.display.update()


# Keep the window open until it is closed

done = False
n = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if not done:
        next_pixel = get_next_pixel()
        if (
            next_pixel[0] < 0
            or next_pixel[0] > screen_width
            or next_pixel[1] < 0
            or next_pixel[1] > screen_height
        ):
            done = True
            print("Done!")
        else:
            is_prime_number = is_prime(n)
            if is_prime_number:
                print(n, next_pixel)
                pygame.draw.rect(
                    screen,
                    red,
                    (
                        next_pixel[0],
                        next_pixel[1],
                        pixel_size,
                        pixel_size,
                    ),
                )
                pygame.display.update()
            n += 1
