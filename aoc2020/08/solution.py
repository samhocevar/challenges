#!/usr/bin/env python

with open('input.txt') as f:
    boot = list(map(str.strip, f))

def run(code, patch=-1):
    pc, acc = 0, 0
    seen = set()
    while pc not in seen and pc < len(code):
        seen.add(pc)
        match code[pc].split():
            case 'nop', n: pc += 1 if pc != patch else int(n)
            case 'acc', n: pc += 1; acc += int(n)
            case 'jmp', n: pc += int(n) if pc != patch else 1
    return pc == len(code), acc

print(run(boot)[1])
print(next(acc for ok, acc in [run(boot, patch) for patch in range(len(boot))] if ok))
