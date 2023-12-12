#!/usr/bin/env python

with open('input.txt') as f:
    data = [(a, tuple(int(n) for n in b.split(','))) for a, b in (l.strip().split() for l in f)]

# Recursive function that computes how many combinations can be made that match
# the rule list. For instance: combinations("????.#...#...", (1,1,1,1)) → 3
def combinations(s, r, n=0, cache=dict()):
    # Handle the easy cases:
    #  - if data is in cache, return the cached value
    #  - if rules are empty, return 1 unless there is still a # in the string, then 0
    #  - if string is too small to possibly match the rules, return 0
    if (s, r) in cache: return cache[(s, r)]
    elif not r: return int('#' not in s)
    elif len(s) < sum(r) + len(r) - 1: return 0
    # We now consider two (or three) different cases:
    #  - if string starts with '.', call combinations() recursively by stripping
    #    the first character and using the same rules.
    #  - if string starts with '#', ensure that there is no '.' in the first
    #    r[0] characters and that the next character, if any, is not a '#',
    #    then call combinations() recursively on the remaining data.
    #  - if string starts with '?', we add the two previous values!
    if s[0] in '.?':
        n += combinations(s[1:], r)
    if s[0] in '#?' and len(s) >= r[0] and '.' not in s[:r[0]] and (len(s) == r[0] or s[r[0]] != '#'):
        n += combinations(s[r[0] + 1:], r[1:])
    cache[(s, r)] = n
    return n

print(sum(combinations(s, r) for s, r in data))
print(sum(combinations('?'.join([s] * 5), r * 5) for s, r in data))
