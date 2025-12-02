# Advent of Code 2025.
# Day 2: Gift Shop

def sum_invalid(lower:int, upper:int) -> int:
    total = 0
    for check in range(lower, upper + 1):
        # print(check)

        check_str = str(check)
        if len(check_str) % 2 == 0: # Even number of digits.
            left_str = check_str[0:(len(check_str) // 2)]
            right_str = check_str[(len(check_str) // 2):]
            # print(left_str, right_str)

            if left_str == right_str:
                total += check
    return total


def new_sum_invalid(lower:int, upper:int) -> int:
    count, total = 0, 0
    found = set()
    for check in range(lower, upper + 1):
        check_str = str(check)

        for length in range(1, 1 + len(check_str) // 2):
            if len(check_str) % length == 0:
                strip = check_str[0:length]
                pieces = len(check_str) // length
                generated = strip * pieces
                # print(check_str, length, strip, pieces, generated)

                if check_str == generated and check not in found:
                    count += 1
                    total += check
                    found.add(check)

    return count, total

assert new_sum_invalid(11,22) == (2, 11 + 22)
assert new_sum_invalid(95,115) == (2, 99 + 111)
assert new_sum_invalid(998,1012) == (2, 999 + 1010)
assert new_sum_invalid(1188511880,1188511890) == (1, 1188511885)
assert new_sum_invalid(222220,222224) == (1, 222222)
assert new_sum_invalid(1698522,1698528) == (0, 0)
assert new_sum_invalid(446443,446449) == (1, 446446)
assert new_sum_invalid(38593856,38593862) == (1, 38593859)
assert new_sum_invalid(565653,565659) == (1, 565656)
assert new_sum_invalid(824824821,824824827) == (1, 824824824)
assert new_sum_invalid(2121212118,2121212124) == (1, 2121212121)

file = open("input.txt", "r")
contents = file.read()

count, total = 0, 0
for pair in contents.split(","):
    lower_str, upper_str = pair.split("-")
    lower, upper = int(lower_str), int(upper_str)
    print(lower, upper, upper - lower)

    co, tot = new_sum_invalid(lower, upper)
    count += co
    total += tot

print(total)
