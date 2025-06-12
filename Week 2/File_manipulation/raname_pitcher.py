# Rename only images in a folder

import os

path = "files"
files = os.listdir(path)

image_files =[]
for file in files:
    if file.endswith((".jpg",".img")):
        image_files.append(file)

for index,file_name in enumerate(image_files):
    
    if file_name.endswith((".jpg",".img")):

        extension = file_name.split(".")[-1]
        
        old_path = os.path.join(path,file_name)
        
        new_name = f"photos_{index+1}.{extension}"
        
        new_path = os.path.join(path,new_name)
        
        os.rename(old_path,new_path)

print("Renaming done...")





