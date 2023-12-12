#!/usr/bin/env python

from re import finditer, subn

with open('input.txt') as f:
    data = [tuple(l.strip().split(' ')[::2]) for l in f]
data, med = data[:-2], data[-1][0]

# Part 1: build a set of all the possible replacement results and print its length
print(len({med[:m.start(0)] + b + med[m.end(0):] for a, b in data for m in finditer(a, med)}))

# Part 2: the general case seems pretty hardcore to solve!
# However we notice the following about the dataset:
#  - there is no rule that transforms Rn, Ar, or Y
#  - whenever Rn appears, it is always followed by Ar
#  - whenever Y appears, it is always between Rn and Ar
#
# Replacing Rn, Y, and Ar with < , > gives the following, more
# human-understandable rules:
#   Ca => PB
#   Ca => P<F>
#   Ca => S<F,F>
#   Ca => P<Mg>
#   F => SiAl
#   H => C<Al>
#   H => C<F,F,F>
#   ...
#
# We also notice that all other rules (that do not create Rn+Ar)
# are of the form 1 atom => 2 atoms. All other atoms are therefore
# strictly interchangeable. We can then apply the following reverse
# transformations:
#   [atom][atom] => [atom]
#   [atom]<[atom]> => [atom]
#   [atom]<[atom],[atom]> => [atom]
#   [atom]<[atom],[atom],[atom]> => [atom]
#
# The final result is just the total number of replacements.
med = med.replace('Rn', '<').replace('Ar', '>').replace('Y', ',')
reduce = 'XX|X<X(,X)*>'.replace('X', '[A-Z][a-z]?')
count = 0
while len(med) > 1:
    med, n = subn(reduce, 'X', med)
    count += n
print(count)
