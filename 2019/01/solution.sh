#!/bin/sh
awk '{x=int($0/3)-2;a+=x;while(x>0){b+=x;x=int(x/3)-2}}END{print a;print b}' < input.txt
