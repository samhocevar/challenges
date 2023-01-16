#!/usr/bin/env python

signal, strength, crt = 1, 0, ''

def parse(f):
    for l in f:
        match l.split():
            case ['addx', x]: yield 0; yield int(x)
            case ['noop']: yield 0

with open('input.txt') as f:
    for cycle, x in enumerate(parse(f), start=1):
        if (cycle + 20) % 40 == 0:
            strength += signal * cycle
        crt += '#' if abs(signal - (cycle - 1) % 40) <= 1 else ' '
        signal += x

print(strength)

for s in range(6):
    print(crt[s*40:][:40])
