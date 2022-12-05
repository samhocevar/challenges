#!/bin/sh

cat input.txt | cut -f2 -d'|' | xargs | tr ' ' '\n' | grep -cv '^.\{5,6\}$'
echo "Not implemented"
