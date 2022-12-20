#!/usr/bin/env python

from collections import defaultdict
from re import findall

graph, parents = defaultdict(dict), defaultdict(set)
with open('input.txt') as f:
    for l in f:
        spec = findall(r'(\d+)? ?(\w+ \w+) bag', l)
        for n, subbag in spec[1:]:
            if n:
                graph[spec[0][1]][subbag] = int(n)
                parents[subbag].add(spec[0][1])

def count_containers(bag):
    todo, containers = set([bag]), set()
    while todo:
        bag = todo.pop()
        new = parents[bag] - containers
        todo |= new
        containers |= new
    return len(containers)

def count_subbags(bag):
    return sum(n * (1 + count_subbags(subbag)) for subbag, n in graph[bag].items())

MYBAG = 'shiny gold'

print(count_containers(MYBAG))
print(count_subbags(MYBAG))
