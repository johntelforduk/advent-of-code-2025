# # Advent of Code 2025.
# Day 4: Printing Department

import pygame
import imageio

def render(g: dict):
    curr_y = 0
    for x, y in g:
        if y != curr_y:
            print()
        print(g[(x, y)], end="")
        curr_y = y
    print("\n")


def find_removal_candidates(grid: dict) -> tuple[dict, int]:
    count = 0
    new_grid = {}
    for x, y in grid:
        if grid[(x, y)] == ".":
            new_grid[(x, y)] = "."
        else:       # Must be a "@"
            adjacent = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == dy == 0:
                        pass
                    else:
                        if (x + dx, y + dy) in grid:
                            if grid[(x + dx, y + dy)] == "@":
                                adjacent += 1

            if adjacent < 4:
                new_grid[(x, y)] = "x"
                count += 1
            else:
                new_grid[(x, y)] = "@"

    return new_grid, count


def remove_candidates(grid: dict) -> dict:
    new_grid = {}
    for x, y in grid:
        if grid[(x, y)] == "x":
            new_grid[(x, y)] = "."
        else:
            new_grid[(x, y)] = grid[(x, y)]
    return new_grid


def render(grid: dict, screen, scale: int, iteration: int, filenames: list):
    black = (0, 0, 0)
    grey = (40, 40, 40)
    green = (0, 255, 0)
    red = (255, 0, 0)
    screen.fill(black)

    for x, y in grid:
        tile_col = grey
        if grid[(x, y)] == "@":
            tile_col = green
        elif grid[(x, y)] == "x":
            tile_col = red
        else:
            tile_col = grey
        pygame.draw.rect(screen, tile_col, pygame.Rect(x * scale, y * scale, scale - 1, scale - 1))

    screenshot_name = f"screenshots/{iteration:05}.png"
    pygame.image.save(screen, screenshot_name)
    filenames.append(screenshot_name)
    pygame.display.flip()


file = open("input.txt", "r")
contents = file.read()

grid = {}
y = 0
for line in contents.split("\n"):
    x = 0
    for cell in line:
        grid[(x, y)] = cell
        x += 1

    y += 1

print(x, y)

scale = 6
screen_size = [scale * x, scale * y]  # [width, height]
pygame.init()                                               # Initialize the game engine.
screen = pygame.display.set_mode(screen_size)

total, count, iteration = 0, 0, 0
filenames = []

while total == 0 or count > 0:
    # render(grid, screen, scale)
    removal_candidates, count = find_removal_candidates(grid)
    total += count
    render(removal_candidates, screen, scale, iteration, filenames)
    print(count)
    grid = remove_candidates(removal_candidates)
    iteration += 1

print(total)
print(filenames)

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('day4.gif', images, fps=5, loop=0)