#File extension count.

import os

folder_path = "files"
file_types = {}

for filename in os.listdir(folder_path):
    if "." in filename:
        ext = filename.split('.')[-1]
        file_types[ext] = file_types.get(ext, 0) + 1

print(" File type count:")
for ext, count in file_types.items():
    print(f"{ext}: {count} files")
