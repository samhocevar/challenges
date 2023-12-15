#!/usr/bin/env python

from itertools import count, takewhile
from functools import cache

fib = cache(lambda n: fib(n - 2) + fib(n - 1) if n >= 2 else n + 1)

print(sum(n for n in takewhile(lambda n: n < 4000000, map(fib, count())) if n % 2 == 0))
