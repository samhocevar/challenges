#!/usr/bin/env python

from functools import reduce
import numpy as np

w, h = 25, 6

with open('input.txt') as f:
    data = list(np.array(list(map(int, l))).reshape((h, w)) for l in zip(*[iter(next(f).strip())] * (w * h)))

best = max(data, key=np.count_nonzero)
print(np.count_nonzero(best == 1) * np.count_nonzero(best == 2))

merged = reduce(lambda a, b: b + (a != 2) * (a - b), data)
for y in range(h):
    print(''.join(" # "[c] for c in merged[y]))
