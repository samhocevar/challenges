#!/usr/bin/env python

from itertools import cycle, permutations

with open('input.txt') as f:
    data = list(map(int, next(f).split(',')))

def execute(mem):
    pc = 0
    def get(op, n):
        return mem[pc + n] if op // pow(10, n + 1) % 10 else mem[mem[pc + n]]
    while True:
        op = mem[pc]
        match op % 100:
            case 1: mem[mem[pc + 3]] = get(op, 1) + get(op, 2); pc += 4
            case 2: mem[mem[pc + 3]] = get(op, 1) * get(op, 2); pc += 4
            case 3: mem[mem[pc + 1]] = yield; pc += 2
            case 4: yield get(op, 1); pc += 2
            case 5:
                if get(op, 1): pc = get(op, 2)
                else: pc += 3
            case 6:
                if not get(op, 1): pc = get(op, 2)
                else: pc += 3
            case 7: mem[mem[pc + 3]] = int(get(op, 1) < get(op, 2)); pc += 4
            case 8: mem[mem[pc + 3]] = int(get(op, 1) == get(op, 2)); pc += 4
            case 99: return

def coroutine(mem, n):
    ret = execute(mem.copy())
    next(ret)
    ret.send(n)
    return ret

for amp_range in [range(5), range(5, 10)]:
    best = 0
    for p in permutations(amp_range):
        amps = [coroutine(data, n) for n in p]
        live = len(amps)
        signal = 0
        for a in cycle(amps):
            signal = a.send(signal)
            try:
                next(a)
            except StopIteration:
                a.close()
                live -= 1
            if live == 0:
                break
        best = max(signal, best)
    print(best)
