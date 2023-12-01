#!/usr/bin/env python

sum1, sum2 = 0, 0

with open('input.txt') as f:
    for line in f:

        if digits := list(map(int, filter(str.isdigit, line))):
            sum1 += 10 * digits[0] + digits[-1]

        def get_digit(pos):
            lut = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            for n, k in enumerate(lut):
                if line[pos:].startswith(k):
                    return n + 1
            if line[pos].isdigit():
                return int(line[pos])

        if digits := list(filter(None, map(get_digit, range(len(line))))):
            sum2 += 10 * digits[0] + digits[-1]

print(sum1)
print(sum2)
