#!/bin/sh
awk '{split($0,c,"");for(i=1;i<=length($0);++i){a[i]+=c[i]}} END{k=1; for(i in a){k*=2;g*=2;g+=a[i]>NR/2} print g*and(k-1,compl(g)) }' < input.txt
echo "Not implemented"
