#!/usr/bin/env python

LUT = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', *map(str, range(1, 10))]

sum1, sum2 = 0, 0

with open('input.txt') as f:
    for line in f:

        # Part 1: just convert all digit characters to integers and take the first and last elements
        if digits := list(map(int, filter(str.isdigit, line))):
            sum1 += 10 * digits[0] + digits[-1]

        # If a number (word or single digit) is found at pos, return its integer value, otherwise None
        def get_digit(pos):
            return next((n % 9 + 1 for n, k in enumerate(LUT) if line[pos:].startswith(k)), None)

        # Part 2: same but use a helper function that also understands words
        if digits := list(filter(None, map(get_digit, range(len(line))))):
            sum2 += 10 * digits[0] + digits[-1]

print(sum1)
print(sum2)
