#!/bin/sh
cat input.txt | tr ABCXYZ 012456 | awk '{a+=$2-3+($2-$1)%3*3} END{print(a)}'
cat input.txt | tr ABCXYZ 234012 | awk '{a+=$2*3+1+($1+$2)%3} END{print(a)}'
