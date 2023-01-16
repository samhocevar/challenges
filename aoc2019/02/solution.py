#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(int, next(f).split(',')))

def compute(data, noun, verb):
    data = data.copy()
    data[1] = noun
    data[2] = verb
    it = iter(data)
    for op in it:
        match op:
            case 1: x = data[next(it)] + data[next(it)]; data[next(it)] = x
            case 2: x = data[next(it)] * data[next(it)]; data[next(it)] = x
            case 99: return data[0]

print(compute(data, 12, 2))

for noun in range(100):
    for verb in range(100):
        if compute(data, noun, verb) == 19690720:
            print(100 * noun + verb)
