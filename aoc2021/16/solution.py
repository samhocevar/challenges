#!/usr/bin/env python

import math
import numpy as np

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
            if b < 0x10:
                return vsum, n
    s = []
    if get_bits(1) == 0:
        stop = get_bits(15) + offset
        while offset < stop:
            s.append(read_packet())
    else:
        s += [read_packet() for _ in range(get_bits(11))]
    vsums, args = zip(*s)
    result = 0
    if tid < 4: # 0 1 2 3  →  + * min max
        result = [sum, math.prod, min, max][tid](args)
    elif tid > 4: # 5 6 7  →  > < ==
        result = int(np.sign(args[0] - args[1]) == tid % 3 - 1)
    return vsum + sum(vsums), result

vsum, result = read_packet()

print(vsum)
print(result)

