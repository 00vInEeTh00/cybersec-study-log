#!/usr/bin/env python3

import hashlib
import os
from datetime import datetime
from jira import JIRA
import sys

file_dir = '/home/eva/Desktop/tools/task3_dir'
hashlog_dir = "/home/eva/Desktop/tools/task3/hash_log.csv"
hash_value = None


# 1. Jira Configuration
EMAIL = "e3630946@gmail.com"
API_TOKEN = "ATATT3xFfGF0nqajnJl1EkoPAi43sSXmag40E0rMGXnjFMVAs5zSjw4NPZV26URS5z481FLUWQNMoHpDj-EIdNckdXJ8WSp7T4Fy_maEy7BFiU3Xg_VLK_aXvydSyvCrBZ4BxnPQAeOoArBbC5CZI6XSp4wPsIisdtTiw8r1ILN5mG--N7ZuUeY=922B711F"
SERVER_URL = "https://e3630946hash-alert.atlassian.net"
PROJECT_KEY = "KAN"    
ISSUE_TYPE = "Incident"

jira = JIRA(server=SERVER_URL, basic_auth=(EMAIL, API_TOKEN))


#Check Directory is exists or not.
if not os.path.isdir(file_dir):
    print(f"Error: Directory {file_dir} does not exist.")
    sys.exit(1)



# 2. Function to calculate file hash
def hashDirectory():
    sha256_hash = hashlib.sha256()

    for root, dirs, files in os.walk(file_dir):
        for filename in sorted(files):
            file_path = os.path.join(root, filename)

            with open(file_path, "rb") as f:
                while chunk :=f.read(8192):
                    sha256_hash.update(chunk) 
    global hash_value                            
    hash_value = sha256_hash.hexdigest()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} Successfully Scanned the directory & Generated hash value.")
    


hashDirectory()
    


#3. Compare current hash with saved hash
def change_detection():
    new_hash = hash_value

    if not os.path.exists(hashlog_dir) or os.stat(hashlog_dir).st_size == 0:
       return False

    with open(hashlog_dir, "r") as retrive:
        lines = retrive.readlines()
    if lines:
        last_line = lines[-1].strip()
        parts = last_line.split()
        old_hash = parts[2]
    if new_hash != old_hash:
        return True
   
    return False

    


#4. Create Jira Incident when change detected
def creating_jira_ticket():
    issue_data = {
        "project": {"key": PROJECT_KEY},
        "summary": f"Hash Change Detected {file_dir}",
        "description": f"The file has changed. \nInvestigation Required.",
        "issuetype": {"name": ISSUE_TYPE}
    }

    issue = jira.create_issue(fields=issue_data)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} Incident Created: ",issue.key)



flag = 0
if change_detection():
    flag=1
    creating_jira_ticket()
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} File Hash Change Detected")
else:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{current_time} No errors were observed, Everything Normal")



def savehash():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if flag == 1:
        detected = "Change_Detected."
        log_line = f"{current_time}  {hash_value}  {detected}\n"
    else:
        log_line = f"{current_time}  {hash_value}\n"
    
    with open(hashlog_dir, "a") as out:
        out.write(log_line)


savehash()









