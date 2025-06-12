# Extract all email id's from log file.

import re

with open("Log.txt" ,"r") as file:
    logs = file.readlines()
for log in logs:
    email_pattern =r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    email = re.findall(email_pattern, log)
    
    if email:
        print(email)

    


   
    #  email -     r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
    # phone  -    r'\b\d{10}\b'
    # ip     -   r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    # password  -  r'Password:\s*(\S+)'
    # date y-m-d   -   r'\b\d{4}-\d{2}-\d{2}\b'
    #  time        -  r'\b\d{2}:\d{2}:\d{2}\b'
    #  ERROR       -  r'ERROR.*'         #  re.IGNORECASE
   

   







