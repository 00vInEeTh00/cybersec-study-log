# Unique ip extrating using regular expression

import re
ip_count = {}

with open("Logs.txt","r") as file:
     content = file.readlines()
    
for line in content:
     ip_pattern =  r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
     ips = re.findall(ip_pattern,line)
     for ip in ips:
          ip_count[ip] = ip_count.get(ip,0) +1

for ip,count in ip_count.items():
     if count ==1:
          print(ip)