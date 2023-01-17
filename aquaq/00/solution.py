#!/usr/bin/env python

T = '2abc3def4ghi5jkl6mno7pqrs8tuv9wxyz0 '
with open('input.txt') as f:
    print(''.join(T[T.index(a) + int(b)] for a, b in map(str.split, f)))
