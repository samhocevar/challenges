#!/usr/bin/env python

from operator import and_, or_, lshift, rshift

with open('input.txt') as f: data = {l[-1]: tuple(l[0:-2]) for l in map(str.split, map(str.strip, f))}

ops = { 'AND': and_, 'OR': or_, 'LSHIFT': lshift, 'RSHIFT': rshift }

def signal(s, cache):
    match cache.get(s) or data.get(s):
        case None: return int(s)
        case (a, op, b): ret = ops[op](signal(a, cache), signal(b, cache))
        case ('NOT', a): ret = ~signal(a, cache)
        case (a,): ret = signal(a, cache)
    cache[s] = (ret, )
    return ret

print(n := signal('a', {}))
print(signal('a', {'b': (n,)}))
