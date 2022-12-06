#!/usr/bin/env python

import re

def matcher(n):
    # (.)(?!\1)(.)(?!\1\2)(.)(?!\1\2\3) ...
    return re.compile(''.join('(.)(?!' + '|'.join('\\'+str(1+j) for j in range(k)) + ')' for k in range(1,n)))

with open('input.txt') as f:
    data = f.read()
    for n in [4, 14]:
        print(n + next(matcher(n).finditer(data)).start(0))
