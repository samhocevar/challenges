#!/usr/bin/env python

import json

with open('input.txt') as f: data = json.loads(next(f))

def flatten(o, everything):
    if isinstance(o, int): yield o
    elif isinstance(o, dict):
        if everything or 'red' not in o.values():
            for v in o.values(): yield from flatten(v, everything)
    elif isinstance(o, list):
        for v in o: yield from flatten(v, everything)

print(sum(flatten(data, True)))
print(sum(flatten(data, False)))
