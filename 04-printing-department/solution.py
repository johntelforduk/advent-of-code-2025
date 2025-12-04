# # Advent of Code 2025.
# Day 4: Printing Department

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

total, count = 0, 0

while total == 0 or count > 0:
    render(grid)
    removal_candidates, count = find_removal_candidates(grid)
    total += count
    render(removal_candidates)
    print(count)
    grid = remove_candidates(removal_candidates)

print(total)
