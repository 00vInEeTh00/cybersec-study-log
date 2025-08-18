#!/usr/bin/bash
 
DIR="$HOME/Desktop/week6/comon_shell/files"
i=1
for file in "$DIR"/*.txt
do
   mv "$file" "$DIR/textfile$i.txt"
   i=$((i+1))
done
