import os
import sys
import timeit
import time

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

size = 1000
pixel_size = 2
edges = []
primes = []
pixel_positions = []


# rechts x+
# links x-
# runter y+
# hoch y-


def get_next_pixel(x, y, direction, edges):
    if direction == "right":
        x += pixel_size
        if x > edges[1]:
            direction = "up"
            edges[1] = x
    elif direction == "left":
        x -= pixel_size
        if x < edges[0]:
            direction = "down"
            edges[0] = x
    elif direction == "down":
        y += pixel_size
        if y > edges[3]:
            direction = "right"
            edges[3] = y
    elif direction == "up":
        y -= pixel_size
        if y < edges[2]:
            direction = "left"
            edges[2] = y
    return (x, y), direction, edges


def fill_pixel_positions():
    direction = "right"
    x, y = size // 2, size // 2
    edges = [x, x, y, y]
    total_pixels = size * size // (pixel_size * pixel_size)
    global pixel_positions
    pixel_positions = [(x, y)]
    start = timeit.default_timer()
    for i in range(total_pixels):
        next_pixel, direction, edges = get_next_pixel(x, y, direction, edges)
        pixel_positions.append(next_pixel)
        x, y = next_pixel
    print(f"Time taken to fill pixel positions: {timeit.default_timer() - start}")


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True


def fill_primes():
    global size, primes
    max_number = size * size
    start = timeit.default_timer()
    primes = [i for i in range(2, max_number - 1) if is_prime(i)]
    print(f"Time taken to fill primes: {timeit.default_timer() - start}")


# Initialize Pygame
pygame.init()

# Set the dimensions of the window
screen = pygame.display.set_mode((size, size))

fill_primes()
fill_pixel_positions()

# Set the color
red = (255, 0, 0)
green = (0, 255, 0)

screen.fill((0, 0, 0))
pygame.draw.rect(
    screen, red, (pixel_positions[0][0], pixel_positions[0][1], pixel_size, pixel_size)
)
pygame.display.update()


# Keep the window open until it is closed

done = False

index = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    index_positions = primes[index]
    if not done:
        if index_positions >= len(pixel_positions):
            done = True
            print("Done")
        else:
            x, y = pixel_positions[index_positions - 1]
            pygame.draw.rect(screen, green, (x, y, pixel_size, pixel_size))
            pygame.display.update()
            index += 1
