#!/usr/bin/env python

r0 = { ')': 3, ']': 57, '}': 1197, '>': 25137 }
r1 = { '(': 1, '[': 2, '{': 3, '<': 4 }

s0 = 0
s1 = []

with open('input.txt') as f:
    for l in f:
        stack = [' ']
        for b in l.strip():
            if b in r0:
                a = stack.pop()
                if ord(b) - ord(a) not in (1, 2):
                    s0 += r0[b]
                    break
            else:
                stack.append(b)
        else:
            n = 0
            while len(stack) > 1:
                n = 5 * n + r1[stack.pop()]
            s1.append(n)

print(s0)
print(sorted(s1)[len(s1)//2])

