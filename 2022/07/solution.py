#!/usr/bin/env python

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
                pwd += (directory,)
        elif line[0] == 'd':
            sizes.setdefault(pwd + (line.split()[1],), 0)
        else:
            sizes[pwd] += int(line.split()[0])

# Accumulate directory sizes using all subdirectories
totalsizes = { dir: sum(size for subdir, size in sizes.items() if subdir[:len(dir)] == dir) for dir in sizes.keys() }
excess = totalsizes[()] - (70000000 - 30000000)

print(sum(x for x in totalsizes.values() if x <= 100000))
print(min(x for x in totalsizes.values() if x >= excess))

