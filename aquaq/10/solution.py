#!/usr/bin/env python

from collections import defaultdict
from heapq import heappush, heappop

fees = defaultdict(list)
with open('input.txt') as f:
    next(f)
    for a, b, fee in map(lambda s: s.split(','), f):
        fees[a] += [(b, int(fee))]

FROM, TO = 'TUPAC', 'DIDDY'

todo = []
done = set()
heappush(todo, (0, FROM))

while todo:
    total, a = heappop(todo)
    if a == TO:
        print(total)
        break
    if a not in done:
        done.add(a)
        for b, fee in fees[a]:
            heappush(todo, (total + fee, b))
