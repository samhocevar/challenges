#!/usr/bin/env python

with open('input.txt') as f:
    cups = [int(c) - 1 for c in next(f).strip()]

def play(cups, rounds, wanted=len(cups)):
    # Build doubly linked list
    nxt, prv = [-1] * len(cups), [-1] * len(cups)
    for i, c in enumerate(cups):
        nxt[c] = cups[(i + 1) % len(cups)]
        prv[c] = cups[(i - 1) % len(cups)]
    def link(a, b): nxt[a], prv[b] = b, a
    # Play all the rounds
    cur = cups[0]
    for _ in range(rounds):
        picked = [nxt[cur], nxt[nxt[cur]], nxt[nxt[nxt[cur]]]]
        link(cur, nxt[picked[-1]])
        dest = (cur - 1) % len(nxt)
        while dest in picked:
            dest = (dest - 1) % len(nxt)
        link(picked[-1], nxt[dest])
        link(dest, picked[0])
        cur = nxt[cur]
    i, ret = 0, []
    while len(ret) < wanted:
        ret.append(i)
        i = nxt[i]
    return ret

ret = play(cups, rounds=100)
print(''.join(str(i + 1) for i in ret))

cups += range(len(cups), 1000000)
ret = play(cups, rounds=10000000, wanted=3)
print((ret[1] + 1) * (ret[2] + 1))
