#!/usr/bin/env python

from itertools import accumulate

pwd = ()
sizes = {(): 0}

with open('input.txt') as f:
    for line in map(str.strip, f):
        if line[0] == '$':
            directory = line[5:]
            if directory == '/':
                pwd = ()
            elif directory == '..':
                pwd = pwd[:-1]
            elif directory:
                pwd = (*pwd, directory)
        else:
            if line[0] == 'd':
                path = (*pwd, line.split()[1])
                if path in sizes:
                    print('OOF')
                sizes[path] = 0
            else:
                s = int(line.split()[0])
                for path in accumulate(map(lambda d: (d,), pwd), initial=()):
                    sizes[path] += s

print(sum(x for x in sizes.values() if x <= 100000))

excess = sizes[()] - (70000000 - 30000000)
print(min(x for x in sizes.values() if x >= excess))

