#!/usr/bin/env python

# Read data into a slightly more usable format:
# "%mp -> gk, kj"  ->  {'mp': ['%', 'gk', 'kj']}
# This means that 'broadcaster' becomes 'roadcaster' but we don’t care
# We also list parents for each node for convenience
with open('input.txt') as f:
    data = {l[0][1:]: [l[0][0], *l[2:]] for l in [l.strip().replace(',', ' ').split() for l in f]}
    parents = {node: {k for k, v in data.items() if node in v[1:]} for node in data}

# Send a list of pulses to the circuit
# 0: high pulse  1: low pulse
def pulse(state, pulses, tracked):
    state[3] += 1
    while pulses:
        src, dst, pulse = pulses.pop()
        state[pulse] += 1
        # Ignore outputs
        if dst not in data: continue
        # If the node is being tracked for cycles, check it
        if pulse and dst in tracked: tracked.discard(dst); state[2] *= state[3]
        # Update states and propagate pulse to children if relevant
        match data[dst][0], pulse:
            case '&', _:
                if pulse: state[dst][0].discard(src)
                else: state[dst][0].add(src)
                pulse = int(state[dst][0] == parents[dst])
            case '%', 1: state[dst][1] ^= 1; pulse = state[dst][1]
            case '%', 0: continue
        for child in data[dst][1:]: pulses.insert(0, (dst, child, pulse))

# state[node][0] contains the set of high parents (used by & nodes)
# state[node][1] is the node on/off state (used by % nodes)
# state[0] and state[1] contain the high and low pulse counts
# state[2] contains the cycle length for part 2
# state[3] contains the current tick count
state = {node: [set(), 1] for node in data} | {0: 0, 1: 0, 2: 1, 3: 0}

# This is the non-generic hack we use for part 2: we know that rx has
# several cycling grandparents, so we track their cycle length and
# eventually print their product.
tracked = set(parents[next(k for k, v in data.items() if 'rx' in v[1:])])

while True:
    pulse(state, [(None, 'roadcaster', 1)], tracked)
    # Part 1: multiply high and low pulse counts
    if state[3] == 1000: print(state[0] * state[1])
    # Part 2: print the product of subcycles
    if not tracked: print(state[2]); break
