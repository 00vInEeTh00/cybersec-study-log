#!/usr/bin/bash

DIR="$HOME/Desktop/week_5/comon_shell/files"
i=1
for file in "$DIR"/*;
do
  if [[ "$file" == *.txt ]]; then
    TEXT_FILES+=("$file")
  elif [[ "$file" == *.png ]]; then
    IMAGES+=("$file")
  fi
done

i=1
for file in "${TEXT_FILES[@]}";
do
  mv "$file" "$DIR/sameName$i.txt"
  i=$((i+1))
done

for file in "${IMAGES[@]}";
do
  mv "$file" "$DIR/sameName$i.png"
  i=$((i+1))
done
