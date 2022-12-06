#!/usr/bin/env python

import math

with open('input.txt') as f:
    data = [int(x, 16) for x in next(f).strip()[::-1]]
offset = 0
remaining = 4

# Read n bits from the bitstream
def get_bits(n):
    global data, offset, remaining
    ret = 0
    offset += n
    while n:
        got = min(remaining, n)
        ret = (ret << got) | ((data[-1] & ((1 << remaining) - 1)) >> (remaining - got))
        remaining -= got
        n -= got
        if remaining == 0:
            data.pop()
            remaining = 4
    return ret

# Decode a packet; return the version sum and the computation result
def read_packet():
    global data, offset, remaining
    vsum = get_bits(3)
    tid = get_bits(3)
    if tid == 4:
        n = 0
        while True:
            b = get_bits(5)
            n = (n << 4) | (b & 0xf)
            if not (b & 0x10):
                return vsum, n
    ltid = get_bits(1)
    s = []
    if ltid == 0:
        l = get_bits(15)
        stop = offset + l
        while offset < stop:
            s.append(read_packet())
    else:
        n = get_bits(11)
        for _ in range(n):
            s.append(read_packet())
    s = list(zip(*s))
    vsum += sum(s[0])
    result = 0
    if tid == 0:
        result = sum(s[1])
    elif tid == 1:
        result = math.prod(s[1])
    elif tid == 2:
        result = min(s[1])
    elif tid == 3:
        result = max(s[1])
    elif tid == 5:
        result = int(s[1][0] > s[1][1])
    elif tid == 6:
        result = int(s[1][0] < s[1][1])
    elif tid == 7:
        result = int(s[1][0] == s[1][1])
    return vsum, result

vsum, result = read_packet()

print(vsum)
print(result)

