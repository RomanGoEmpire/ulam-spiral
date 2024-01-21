import os
import sys
import timeit
import time

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

SIZE = 1000
PIXEL_SIZE = 2


def get_next_pixel(x: int, y: int, direction: str, edges: list) -> tuple:
    if direction == "right":
        x += PIXEL_SIZE
        if x > edges[1]:
            direction = "up"
            edges[1] = x
    elif direction == "left":
        x -= PIXEL_SIZE
        if x < edges[0]:
            direction = "down"
            edges[0] = x
    elif direction == "down":
        y += PIXEL_SIZE
        if y > edges[3]:
            direction = "right"
            edges[3] = y
    elif direction == "up":
        y -= PIXEL_SIZE
        if y < edges[2]:
            direction = "left"
            edges[2] = y
    return (x, y), direction, edges


def fill_pixel_positions() -> list:
    direction = "right"
    x, y = SIZE // 2, SIZE // 2
    edges = [x, x, y, y]
    total_pixels = SIZE * SIZE // (PIXEL_SIZE * PIXEL_SIZE)
    pixel_positions = [(x, y)]
    start = timeit.default_timer()
    for i in range(total_pixels):
        next_pixel, direction, edges = get_next_pixel(x, y, direction, edges)
        pixel_positions.append(next_pixel)
        x, y = next_pixel
    print(f"Time taken to fill pixel positions: {timeit.default_timer() - start}")
    return pixel_positions


def is_prime(n: int) -> bool:
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):  # only odd numbers
        if n % i == 0:
            return False
    return True


def fill_primes() -> list:
    global SIZE
    max_number = SIZE * SIZE
    start = timeit.default_timer()
    primes = [i for i in range(2, max_number - 1) if is_prime(i)]
    print(f"Time taken to fill primes: {timeit.default_timer() - start}")
    return primes


pygame.init()
pygame.display.set_caption("Ulam Spiral")
screen = pygame.display.set_mode((SIZE, SIZE))

primes = fill_primes()
pixel_positions = fill_pixel_positions()


red = (255, 0, 0)
green = (0, 255, 0)

# Draw the first pixel
pygame.draw.rect(
    screen, red, (pixel_positions[0][0], pixel_positions[0][1], PIXEL_SIZE, PIXEL_SIZE)
)
pygame.display.update()

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
            pygame.draw.rect(screen, green, (x, y, PIXEL_SIZE, PIXEL_SIZE))
            pygame.display.update()
            index += 1
