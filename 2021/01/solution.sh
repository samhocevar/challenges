#!/bin/sh
awk '{q+=(NR>3 && $1>a);p+=(NR>1 && $1>c);a=b;b=c;c=$1} END{print(p"\n"q)}' < input.txt
