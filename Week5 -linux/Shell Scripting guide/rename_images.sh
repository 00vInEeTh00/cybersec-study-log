#!/usr/bin/bash

DIR="$HOME/Desktop/files"
i=1
for file in "$DIR"/*.png
do
   mv "$file" "$DIR/newName$i.png"
   i=$((i+1))
done
