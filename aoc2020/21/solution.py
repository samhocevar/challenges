#!/usr/bin/env python

from collections import defaultdict
from functools import reduce
from operator import and_, or_
import re

lines = []
lut = defaultdict(list)
with open('input.txt') as f:
    for l in map(str.strip, f):
        a, b = re.match('(.*) \(contains (.*)\)', l).groups()
        lines.append({*a.split()})
        for allergen in b.split(', '):
            lut[allergen].append(lines[-1])

# Part 1

# Print all ingredients that are not valid candidates. Valid candidates are
# the ones that appear in all foods listing a given allergen.
candidates = reduce(or_, (reduce(and_, ingredients) for ingredients in lut.values()))
print(sum(len(s - candidates) for s in lines))

# Part 2

# Build dictionary of allergens by starting with keeping only valid candidates
allergens = {a: candidates & reduce(and_, l) for a, l in lut.items()}
while any(len(s) > 1 for s in allergens.values()):
    found = reduce(or_, (s for s in allergens.values() if len(s) == 1))
    for a, s in allergens.items():
        if len(s) > 1:
            s -= found
print(','.join(list(zip(*sorted((k, *v) for k, v in allergens.items())))[1]))
