#!/usr/bin/env python

decks = []
with open('input.txt') as f:
    for l in map(str.strip, f):
        if l[:1] == 'P': decks.append(())
        elif l: decks[-1] += (int(l),)

def play1(a, b):
    while a and b:
        ca, cb, a, b = a[0], b[0], a[1:], b[1:]
        if ca > cb:
            a += (ca, cb)
        else:
            b += (cb, ca)
    return sum(n * p for n, p in enumerate((a + b)[::-1], 1))

def play2(a, b, first_game=True):
    seen = set()
    while a and b and (*a, -1, *b) not in seen:
        seen.add((*a, -1, *b))
        ca, cb, a, b = a[0], b[0], a[1:], b[1:]
        if ca <= len(a) and cb <= len(b):
            a_wins = play2(a[:ca], b[:cb], False)
        else:
            a_wins = ca > cb
        if a_wins:
            a += (ca, cb)
        else:
            b += (cb, ca)
    if first_game:
        return sum(n * p for n, p in enumerate((a + b)[::-1], 1))
    return bool(a)

print(play1(*decks))
print(play2(*decks))
