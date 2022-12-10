#!/usr/bin/env python

from collections import defaultdict
from itertools import accumulate

cwd = ()
sizes = defaultdict(int)

with open('input.txt') as f:
    for line in map(str.strip, f):
        match line.split():
            case '$', 'cd', '..': cwd = cwd[:-1]
            case '$', 'cd', '/': cwd = ()
            case '$', 'cd', directory: cwd += (directory,)
            case '$' | 'dir', _: pass
            case size, _ if int(size):
                for path in accumulate(zip(cwd), initial=()):
                    sizes[path] += int(size)

excess = sizes[()] - (70000000 - 30000000)

print(sum(x for x in sizes.values() if x <= 100000))
print(min(x for x in sizes.values() if x >= excess))

