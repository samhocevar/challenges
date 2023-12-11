#!/usr/bin/env python

from itertools import count
from hashlib import md5

with open('input.txt') as f: data = next(f).strip()

for prefix in ('00000', '000000'):
    print(next(n for n in count() if md5((data + str(n)).encode('ascii')).hexdigest().startswith(prefix)))

