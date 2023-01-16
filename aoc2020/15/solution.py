#!/usr/bin/env python

with open('input.txt') as f:
    data = list(map(int, next(f).split(',')))

def compute(limit):
    history = {spoken: n for n, spoken in enumerate(data, 1)}
    last = data[-1]
    for n in range(len(data), limit):
        history[last], last = n, n - history.get(last, n)
    print(last)

compute(2020)
compute(30000000)
