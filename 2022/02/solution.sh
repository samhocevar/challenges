#!/bin/sh

# For moves:
#   0: rock  1: paper  2: scissors
# For outcomes:
#   0: loss  1: draw  2: win

# $1: opponent move  $2: player move
# 1+$2 → score for playing
# (4+$2-$1)%3*3 → score for outcome

# $1: opponent move  $2: outcome
# ($1+$2+2)%3 = what we should play
# 1+($1+$2+2)%3 → score for playing
# (4+($1+$2+2)%3-$1)%3*3 = $2*3 → score for outcome

cat input.txt | tr ABCXYZ 012012 | awk '{a+=1+$2+($2-$1+4)%3*3;b+=1+($1+$2+2)%3+$2*3} END{print a"\n"b}'
