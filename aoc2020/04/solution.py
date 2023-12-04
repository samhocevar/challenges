#!/usr/bin/env python

from re import fullmatch

required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

s0, s1 = 0, 0
with open('input.txt') as f:
    for passport in f.read().split('\n\n'):
        fields = passport.replace('\n', ' ').split()
        if not required.issubset({f[:3] for f in fields}):
            continue
        s0 += 1
        for f in fields:
            match f.split(':'):
                case 'byr', s:
                    if not fullmatch('[0-9]{4}', s) or int(s) < 1920 or int(s) > 2002: break
                case 'iyr', s:
                    if not fullmatch('[0-9]{4}', s) or int(s) < 2010 or int(s) > 2020: break
                case 'eyr', s:
                    if not fullmatch('[0-9]{4}', s) or int(s) < 2020 or int(s) > 2030: break
                case 'hgt', s:
                    if not fullmatch('([0-9]{3}cm|[0-9]{2}in)', s): break
                    if s[3] == 'c' and (int(s[:3]) < 150 or int(s[:3]) > 193): break
                    if s[3] == 'i' and (int(s[:2]) < 59 or int(s[:2]) > 76): break
                case 'hcl', s:
                    if not fullmatch('#[0-9a-f]{6}', s): break
                case 'ecl', s:
                    if not fullmatch('(amb|blu|brn|gry|grn|hzl|oth)', s): break
                case 'pid', s:
                    if not fullmatch('[0-9]{9}', s): break
        else:
            s1 += 1
print(s0)
print(s1)
