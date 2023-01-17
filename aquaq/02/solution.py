#!/usr/bin/env python

out = []
with open('input.txt') as f:
    data = list(map(int, *map(str.split, f)))[::-1]
    while data:
        out.append(data[-1])
        data = data[:data.index(out[-1])]
print(sum(out))
