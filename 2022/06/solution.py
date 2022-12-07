#!/usr/bin/env python

# Read data using a sliding window of size n (zip + slices)
# Get the first index where n different characters are found (len(set) == n)

data = open('input.txt').read()
for n in [4, 14]:
    print(n + next(pos for pos, window in enumerate(zip(*(data[i:] for i in range(n)))) if len(set(window)) == n))
