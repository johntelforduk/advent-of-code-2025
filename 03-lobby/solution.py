# Advent of Code 2025.
# Day 3: Lobby

def highest(s: str, check: str) -> str|None:
    position = None
    for pos, digit in enumerate(s):
        if digit == check:
            if position is None:
                position = pos

    if position is None:
        return None

    remaining = s[position + 1:]
    return remaining


assert highest("811111111111119", "9") == ""
assert highest("432563", "6") == "3"
assert highest("2189221", "9") == "221"
assert highest("23", "3") == ""
assert highest("1", "1") == ""
assert highest("55555", "5") == "5555"
assert highest("1111222", "2") == "22"
assert highest("99991", "9") == "9991"


def high_list(s: str) -> list:
    output = []
    for try_digit in range(9, 0, -1):
        remaining = highest(s, str(try_digit))
        if remaining is not None:
            output.append((str(try_digit), remaining))
    return output


assert high_list("811111111111119") == [("9", ""), ("8", "11111111111119"), ("1", "1111111111119")]


def largest_joltage(found: str, remaining: str, target_length: int) -> str:
    if len(found) == target_length:
        return found

    if len(found) + len(remaining) < target_length:
        return ""

    search_space = high_list(remaining)
    for digit, new_remaining in search_space:
        candidate = found + digit
        try_it = largest_joltage(candidate, new_remaining, target_length)
        if len(try_it) == target_length:
            return try_it

    return ""

assert largest_joltage("", "987654321111111", 2) == "98"
assert largest_joltage("", "811111111111119", 2) == "89"
assert largest_joltage("", "234234234234278", 2) == "78"
assert largest_joltage("", "818181911112111", 2) == "92"

assert largest_joltage("", "987654321111111", 12) == "987654321111"
assert largest_joltage("", "811111111111119", 12) == "811111111119"
assert largest_joltage("", "234234234234278", 12) == "434234234278"
assert largest_joltage("", "818181911112111", 12) == "888911112111"

file = open("input.txt", "r")
contents = file.read()

total = 0
for line in contents.split("\n"):
    total += int(largest_joltage("", line, 12))

print(total)
