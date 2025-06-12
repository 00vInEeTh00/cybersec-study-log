#  Search a Keyword in Multiple Text Files

import os

folder_path = "files"
keyword = "sample"

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as f:
            contents = f.read()
            if keyword in contents:
                print(f" Found in: {filename}")
            else:
                print("Item not found..")
