def ascii_render(g: dict):
    curr_y = 0
    for x, y in g:
        if y != curr_y:
            print()
        print(g[(x, y)], end="")
        curr_y = y
    print("\n")


def dict_add_or_create(g: dict, key: str, value: str):
    if key in g:
        g[key] = g[key] + value
    else:
        g[key] = value

g = {}
dict_add_or_create(g, "x", 5)
assert g == {"x": 5}
dict_add_or_create(g, "x", 67)
assert g == {"x": 72}

# Load file contents into a grid dictionary.
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

beams = {}

# Find the starting beam.
x = 0
while len(beams) == 0:
    if grid[(x, 0)] == "S":
        beams[x] = 1
    x +=1

lit_grid = grid.copy()

y = 1
splits = 0

all_beams = {}
most_common = 0

while (0, y) in lit_grid:
    new_beams = {}
    x = 0

    while (x, y) in lit_grid:

        if x in beams:
            if lit_grid[(x, y)] == "^":                         # We found a splitter, and there is a beam going into it.
                dict_add_or_create(new_beams, x - 1, beams[x])  # Beam splits left.
                dict_add_or_create(new_beams, x + 1, beams[x])  # Beam splits right.

                splits += 1                                     # Keep count of splits for Part 1.

                lit_grid[(x - 1, y)] = "|"                      # Put "|"s into grid for later printout.
                lit_grid[(x + 1, y)] = "|"

            else:       # This beam that doesn't go into a splitter.
                dict_add_or_create(new_beams, x, beams[x])
                lit_grid[(x, y)] = "|"                          # Put "|" into grid for later printout.

        x += 1

    beams = new_beams.copy()
    all_beams[y] = beams
    most_common = max(most_common, max(beams.values()))

    y += 1

ascii_render(lit_grid)

print("Part 1:", splits)
print("Part 2:", sum(beams.values()))

print(most_common)


import pygame
import matplotlib.cm as cm

def value_to_rgb_heatmap_matplotlib(value, cmap_name="cividis"):
    value = max(0, min(255, value))

    # Normalize value to 0.0 - 1.0.
    norm_val = value / 255.0

    # Get the colormap
    cmap = cm.get_cmap(cmap_name)

    # Get the RGBA color from the colormap (0.0-1.0 floats)
    # The colormap function takes a normalized value and returns (R, G, B, A)
    r, g, b, _ = cmap(norm_val) # We ignore the alpha channel here

    # Convert 0.0-1.0 RGB floats to 0-255 integer RGB tuple
    return (int(r * 255), int(g * 255), int(b * 255))


scale = 8
screen_size = [scale * x, scale * y]  # [width, height]
pygame.init()                                               # Initialize the game engine.
screen = pygame.display.set_mode(screen_size)

black = (0, 0, 0)
screen.fill(black)

for y in all_beams:
    highest = max(all_beams[y].values())

    for x in all_beams[y]:
        value = all_beams[y][x]
        intensity = 255 * all_beams[y][x] // highest
        colour = value_to_rgb_heatmap_matplotlib(intensity)
        pygame.draw.rect(screen, colour, pygame.Rect(x * scale, y * scale, scale - 1, scale - 1))

pygame.display.flip()
pygame.image.save(screen, "day07.png")
