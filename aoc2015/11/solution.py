#!/usr/bin/env python

with open('input.txt') as f:
    data = [ord(c) - ord('a') for c in next(f).strip()][::-1]

def check(l):
    c1, c2, c3 = False, False, False
    for n in range(len(l)):
        if c1:
            if n >= 2 and l[n] == l[n - 1] and l[n] != l[n - 2]:
                c2 = True
        else:
            if n >= 1 and l[n] == l[n - 1]:
                c1 = True
        if n >= 2 and l[n - 2] - l[n - 1] == 1 and l[n - 1] - l[n] == 1:
           c3 = True
    return c2 and c3

def update(l):
    while True:
        # Increment first letter of password
        l[0] += 1
        # Update carry
        for n in range(len(l)):
            if l[n] >= 26:
                l[n] = 0
                l[n + 1] += 1
            else:
                # If 'l', 'o' or 'i' appear in the password, skip the entire range
                if l[n] in [8, 11, 14]:
                    l[n] += 1
                    for k in range(n):
                        l[k] = 0
                break
        # Check validity
        if check(l):
            return l

pwd = update(data.copy())
print(''.join(chr(ord('a') + c) for c in pwd)[::-1])
print(''.join(chr(ord('a') + c) for c in update(pwd))[::-1])
