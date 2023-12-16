#!/usr/bin/env python

from collections import Counter

with open('input.txt') as f: data = [l.strip() for l in f]

print(''.join(Counter(l).most_common(1)[0][0] for l in zip(*data)))
print(''.join(Counter(l).most_common()[-1][0] for l in zip(*data)))
