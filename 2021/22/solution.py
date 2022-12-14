#!/usr/bin/env python

import re

state = set()
small = True

def try_split(a, b):
    for d in (0, 2, 4):
        if b[d] > a[d]:
            yield a[:d] + (a[d], b[d] - 1) + a[d+2:]
            yield a[:d] + (b[d], a[d+1]) + a[d+2:]
            return
        elif b[d+1] < a[d+1]:
            yield a[:d] + (a[d], b[d+1]) + a[d+2:]
            yield a[:d] + (b[d+1] + 1, a[d+1]) + a[d+2:]
            return

def print_state():
    print(sum((b[1] - b[0] + 1) * (b[3] - b[2] + 1) * (b[5] - b[4] + 1) for b in state))

with open('input.txt') as f:
    for l in f:
        on = l[1] == 'n'
        b = tuple(map(int, re.findall("-?[0-9]+", l)))

        if small and any(abs(x) > 50 for x in b):
            print_state()
            small = False

        newstate = set()
        while state:
            a = state.pop()
            if b[0] > a[1] or a[0] > b[1] or b[2] > a[3] or a[2] > b[3] or b[4] > a[5] or a[4] > b[5]:
                newstate.add(a)
            else:
                for a2 in try_split(a, b):
                    state.add(a2)
        if on:
            newstate.add(b)
        state = newstate

print_state()
