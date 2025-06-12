# Rename only images in a folder 

import os

path = "files" #file stored folder
files=os.listdir(path) #get all files list

for index, filename in enumerate(files):

    old_path=os.path.join(path,filename)
    # Gets file path & name

    new_name = f"document_{index+1}.txt"
    #create new file name

    new_path = os.path.join(path,new_name)
    #joined path & new name

    os.rename(old_path,new_path)
    #change old path/name to new path/name

print("All files are renamed successfully")
