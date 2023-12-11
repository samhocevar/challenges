#!/usr/bin/env python

# The shuffle procedure is actually just a series of multiplications and additions
# modulo the deck size, so we can reduce it to a single multiplication and addition
# of the form: x → a·x + b
with open('input.txt') as f:
    a, b = 1, 0
    for l in f:
        if   'new' in l: a, b = -a, -b - 1
        elif 'inc' in l: a, b = a * int(l[20:]), b * int(l[20:])
        elif 'cut' in l: b -= int(l[4:])

# Part 1: track position of card 2019 along the shuffle
print((2019 * a + b) % 10007)

# Part 2: the final formula when performing x → a·x + b multiple times is:
#   xₙ = aⁿx₀ + (1-aⁿ)/(1-a)·b
# Since we want to know what x₀ will give xₙ = 2020, we invert the formula:
#   xₒ = a⁻ⁿ·(xₙ-(1-aⁿ)/(1-a)·b)
size, n = 119315717514047, 101741582076661
print(pow(a, -n, size) * (2020 - (1 - pow(a, n, size)) * pow(1 - a, -1, size) * b) % size)
