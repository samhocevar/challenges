#!/usr/bin/env python

import re

with open('input.txt') as f:
    r = list(map(int, next(f).split('-')))

r1 = re.compile(r'^0*1*2*3*4*5*6*7*8*9*$')
r2 = re.compile(r'(.)\1')
r3 = re.compile(r'(^|(.)(?!\2))(.)\3(?!\3)')

print(sum(1 for n in range(r[0], r[1] + 1) if r1.match(str(n)) and r2.search(str(n))))
print(sum(1 for n in range(r[0], r[1] + 1) if r1.match(str(n)) and r3.search(str(n))))

