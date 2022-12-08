#!/usr/bin/env python

from itertools import accumulate

cwd = ()
sizes = {(): 0}

with open('input.txt') as f:
    for line in map(str.strip, f):
        if line[0] == '$':
            directory = line[5:]
            if directory == '/':
                cwd = ()
            elif directory == '..':
                cwd = cwd[:-1]
            elif directory:
                cwd += (directory,)
        elif line[0] == 'd':
            name = line.split()[1]
            sizes[cwd + (name,)] = 0
        else:
            size = int(line.split()[0])
            for path in accumulate(map(lambda d: (d,), cwd), initial=()):
                sizes[path] += size


excess = sizes[()] - (70000000 - 30000000)

print(sum(x for x in sizes.values() if x <= 100000))
print(min(x for x in sizes.values() if x >= excess))

