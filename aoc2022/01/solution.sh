#!/bin/sh
awk '{a+=$0} /^$/{print(a);a=0} END{print(a)}' < input.txt | sort -n | tail -n3 | awk '{a+=$0} END{print$0"\n"a}'
