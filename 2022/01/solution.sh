#!/bin/sh
cat input.txt | awk '{a+=$0} /^$/{print(a);a=0} END{print(a)}' | sort -n | tail -n3 | awk '{a+=$0} END{print$0"\n"a}'
