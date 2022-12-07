#!/bin/sh
awk '/^f/{x+=$2; yy+=y*$2} /^u/{y-=$2} /^d/{y+=$2} END{print x*y"\n"x*yy}' < input.txt
