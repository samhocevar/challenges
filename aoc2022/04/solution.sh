#!/bin/sh
awk -F',|-' '{a+=($1-$3)*($2-$4)<=0;b+=$2>=$3&&$4>=$1} END{print a"\n"b}' < input.txt
