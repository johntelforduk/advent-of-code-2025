# Advent of Code 2025.
# Day 1: Secret Entrance.

def safe(start: int, direction: str, clicks: int):
    if direction == "L":
        output = (start - clicks) % 100
    else:
        output = (start + clicks) % 100
    return output

def nudge(start: int, direction: str, clicks: int):
    position = start
    count = 0
    for each in range(clicks):
        position = safe(position, direction, 1)
        if position == 0:
            count += 1
    return position, count

assert safe(11, "R", 8) == 19
assert safe(0, "L", 1) == 99
assert safe(99, "R", 1) == 0
assert safe(5, "L", 10) == 95
assert safe(95, "R", 5) == 0

file = open("input.txt", "r")
contents = file.read()

rows = contents.split("\n")
print(rows)

current = 50
count = 0

for each_row in rows:
    direction = each_row[0]
    clicks = int(each_row[1:])
    current, zeroes = nudge(current, direction, clicks)
    print(current, zeroes)
    count += zeroes

print(count)
