#!/usr/bin/env python

from heapq import heappush, heappop

# Read input as [HP, damage]
with open('input.txt') as f: data = [int(l.split()[-1]) for l in f]

# Use pathfinding to optimise for mana spending
def optimise(hard_mode):
    todo, done = [(0, (data[0], 500, 50, 0, 0, 0))], set()
    while todo:
        cost, state = heappop(todo)
        if state not in done:
            done.add(state)
            boss_hp, mana, ply_hp, shield, poison, charge = state
            # Do a boss turn (unless it’s the very beginning of the fight) then a player turn
            for boss_turn in [True, False] if cost else [False]:
                if poison: boss_hp -= 3
                if charge: mana += 101
                if boss_hp <= 0: return cost
                ply_hp -= max(1, data[1] - (7 if shield else 0)) if boss_turn else hard_mode
                if ply_hp <= 0: break
                poison = max(0, poison - 1)
                charge = max(0, charge - 1)
                shield = max(0, shield - 1)
            # Choose a player action
            if ply_hp <= 0 or mana < 53: continue
            if mana >= 53: heappush(todo, (cost + 53, (boss_hp - 4, mana - 53, ply_hp, shield, poison, charge)))
            if mana >= 73: heappush(todo, (cost + 73, (boss_hp - 2, mana - 73, ply_hp + 2, shield, poison, charge)))
            if mana >= 113 and not shield: heappush(todo, (cost + 113, (boss_hp, mana - 113, ply_hp, 6, poison, charge)))
            if mana >= 173 and not poison: heappush(todo, (cost + 173, (boss_hp, mana - 173, ply_hp, shield, 6, charge)))
            if mana >= 229 and not charge: heappush(todo, (cost + 229, (boss_hp, mana - 229, ply_hp, shield, poison, 5)))

print(optimise(0))
print(optimise(1))
