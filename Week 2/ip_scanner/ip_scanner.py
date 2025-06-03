import os

for i in range(1,21):
    ip = f" 192.168.1.{i}"
    
    response = os.system(f"ping -n 1 -w 1000 {ip} > nul")
    
    if response == 0:
       print(f"{ip} is online")
    else:
       print(f"{ip} is offline")

 