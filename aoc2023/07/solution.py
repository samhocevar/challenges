#!/usr/bin/env python

from re import search

# List of regexes that match five of a kind, four of a kind, etc. (string must be sorted)
types = [r'(.)\1{4}', r'(.)\1{3}', r'(.)\1\1(.)\2|(.)\3(.)\4\4', r'(.)\1\1', r'(.)\1.?(.)\2', r'(.)\1', '.']

# The score() function returns the type of hand, from 0 (high card) to 6 (five of a kind)
score = lambda s: next(6 - n for n, t in enumerate(types) if search(t, ''.join(sorted(s))))

# Read data as a list of (hand, bid) tuples and rewrite faces so that they are now
# lexicographically ordered and comparing them becomes easy
with open('input.txt') as f:
    data = [(h.translate(str.maketrans('AKQJT', 'MLKJI')), int(b)) for h, b in (l.split() for l in f)]

# Part 1: sort hands by their score, breaking ties with lexicographic order
print(sum(n * t[1] for n, t in enumerate(sorted(data, key=lambda t: (score(t[0]), t[0])), 1)))

# Part 2: do the same, but find the best score by replacing 'J' with every card in
# the hand, and break ties by replacing 'J' with '1'
print(sum(n * t[1] for n, t in enumerate(sorted(data, key=lambda t: (max(score(t[0].replace('J', c)) for c in t[0]), t[0].replace('J', '1'))), 1)))

