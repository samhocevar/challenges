#!/usr/bin/env python

print(max(n for n in [a * b for a in range(100, 1000) for b in range(a, 1000)] if int(str(n)[::-1]) == n))

