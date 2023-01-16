#!/usr/bin/env python

from math import prod
import re

data = []
with open('input.txt') as f:
    for l in map(str.strip, f):
        data.append(re.split("(?=[()*+])|(?=\d)(?<=[()*+])", l.replace(' ', '')))
        if data[-1][0] == '': # Workaround for a bug in the split regex...
            data[-1] = data[-1][1:]

def part1_val(it):
    match next(it):
        case '(': return part1_expr(it)
        case s: return int(s)

def part1_expr(it):
    ret = part1_val(it)
    while it:
        match next(it, None):
            case ')': return ret
            case '+': ret += part1_val(it)
            case '*': ret *= part1_val(it)
            case None: return ret
    return ret

def part1(expr):
    return part1_expr(iter(expr))

print(sum(part1(expr) for expr in data))

def part2_val(it):
    a, b = next(it)
    match a:
        case '(': ret, b = part2_expr(it); _, b = next(it); return ret, b
        case s: return int(s), b

def part2_sum(it):
    a, b = part2_val(it)
    ret = [a]
    while True:
        match b:
            case '+': _ = next(it); a, b = part2_val(it); ret.append(a)
            case x: return sum(ret), b

def part2_expr(it):
    a, b = part2_sum(it)
    ret = [a]
    while True:
        match b:
            case '*': _ = next(it); a, b = part2_sum(it); ret.append(a)
            case x: return prod(ret), b

def part2(expr):
    ret, _ = part2_expr(zip(iter(expr), iter(expr[1:] + [None])))
    return ret

print(sum(part2(expr) for expr in data))
