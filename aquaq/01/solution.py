#!/usr/bin/env python

import re

with open('input.txt') as f:
    c = re.sub('[^a-f0-9]', '0', next(f).strip())
    n = (len(c) + 2) // 3
    print(c[0:2] + c[n:n+2] + c[n*2:n*2+2])
