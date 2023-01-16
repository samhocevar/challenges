#!/usr/bin/env python

from itertools import takewhile
import numpy as np

with open('input.txt') as f:
    dots = [(int(y), int(x)) for x, y in [l.strip().split(',') for l in takewhile(str.strip, f)]]
    w, h = 1 + max(x for y, x in dots), 1 + max(y for y, x in dots)
    m = np.zeros(w * h).reshape(h, w)
    for a in dots:
        m[a] = 1

    started = False
    folds = [(s[0], int(s[2:])) for s in [l.strip().split(' ')[2] for l in f]]
    for axis, z in folds:
        if axis == 'y':
            top = np.pad(m[:z], ((max(h - 2 * z - 1, 0), 0), (0, 0)), mode='constant', constant_values=0)
            bot = np.pad(m[z+1:], ((0, max(2 * z - h + 1, 0)), (0, 0)), mode='constant', constant_values=0)
            m = top + bot[::-1]
            h = m.shape[0]
        else:
            left = np.pad(m[:,:z], ((0, 0), (max(w - 2 * z - 1, 0), 0)), mode='constant', constant_values=0)
            right = np.pad(m[:,z+1:], ((0, 0), (0, max(2 * z - w + 1, 0))), mode='constant', constant_values=0)
            m = left + right[:,::-1]
            w = m.shape[1]
        if not started:
            print(np.count_nonzero(m))
            started = True

for k in m:
    print(''.join('@' if x else ' ' for x in k))
