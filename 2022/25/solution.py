#!/usr/bin/env python

def decode(s):
    return sum(("=-012".index(c) - 2) * pow(5, n) for n, c in enumerate(s[::-1]))

def encode(n, s=''):
    while n or not s:
        k = (n + 2) % 5
        s, n = "=-012"[k] + s, (n - k + 2) // 5
    return s

with open('input.txt') as f:
    print(encode(sum(map(decode, map(str.strip, f)))))
