#!/bin/sh
cat input.txt | awk '{a+=$0} /^$/{print(a);a=0} END{print(a)}' | sort -n | tail -n 1
cat input.txt | awk '{a+=$0} /^$/{print(a);a=0} END{print(a)}' | sort -n | tail -n 3 | awk '{a+=$0} END{print(a)}'
