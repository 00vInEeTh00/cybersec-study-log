# Organize Files by Type into Folders
# Moving files using shutil

import os
import shutil

source_folder = "files"
destination_folder = "moved"

for filename in os.listdir(source_folder):
    if "." in filename:
        ext = filename.split('.')[-1]
        ext_folder = os.path.join(destination_folder, ext)

        # Create folder if not exists
        os.makedirs(ext_folder, exist_ok=True)

        shutil.move(os.path.join(source_folder, filename),
                    os.path.join(ext_folder, filename))

print(" Files organized by type")
