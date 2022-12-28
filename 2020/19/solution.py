#!/usr/bin/env python

import re
import regex

rules = {}
strings = []

with open('input.txt') as f:
    for l in map(str.strip, f):
        if not l:
            break
        s = l.split(':')
        rules[s[0]] = s[1].strip()
    for l in map(str.strip, f):
        strings.append(l)

def build(n):
    match rules[n].split():
        case ['R8']: return f'({build("42")})+' # Special rule for part 2
        case ['R11']: return f'(?<left>{build("42")}(?&left)?{build("31")})' # Recursive regex rule for part 2
        case ['"a"' | '"b"']: return rules[n][1]
        case x, y, '|', z, t: return f'({build(x)}{build(y)}|{build(z)}{build(t)})'
        case x, '|', y: return f'({build(x)}|{build(y)})'
        case l: return ''.join(map(build, l))

r1 = re.compile('^' + build('0') + '$')
print(sum(1 for s in strings if r1.match(s)))

rules['8'] = 'R8'
rules['11'] = 'R11'
r2 = regex.compile('^' + build('0') + '$')
print(sum(1 for s in strings if r2.match(s)))
