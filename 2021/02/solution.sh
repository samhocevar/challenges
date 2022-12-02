#!/bin/sh
awk '/forward/{x+=$2; yy+=y*$2} /up/{y-=$2} /down/{y+=$2} END{print x*y"\n"x*yy}' < input.txt
