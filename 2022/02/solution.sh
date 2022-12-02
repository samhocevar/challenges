#!/bin/sh

# 0: rock  1: paper  2: scissors

# $1: opponent  $2: player
# (4+$2-$1)%3 → 0=loss 1=draw 2=win
cat input.txt | tr ABCXYZ 012012 | awk '{a+=(1+$2)+(4+$2-$1)%3*3} END{print(a)}'

# $1: opponent  $2: outcome
# x+0: for a draw  x+1: for a win  x+2: for a loss
cat input.txt | tr ABCXYZ 012201 | awk '{x=($1+$2)%3; a+=(1+x)+(4+x-$1)%3*3} END{print(a)}'
