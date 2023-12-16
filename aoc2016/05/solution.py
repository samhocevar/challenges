#!/usr/bin/env python

from itertools import count, islice
from hashlib import md5

with open('input.txt') as f: data = f.read().strip()

# List the 6th and 7th characters of all compliant hashes
def hack(): yield from (f[5:7] for f in (md5((data + str(n)).encode('ascii')).hexdigest() for n in count()) if f.startswith('00000'))

# Part 1: just join the first 8 characters
print(''.join(islice((s[0] for s in hack()), 8)))

# Part 2: build the password until it is complete
pwd = {}
for s in hack():
    if s[0] in '01234567': pwd = {s[0]: s[1]} | pwd
    if len(pwd) == 8: print(''.join(tuple(zip(*sorted(pwd.items())))[1])); break
