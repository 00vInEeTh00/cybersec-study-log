import pandas as pd
import matplotlib.pyplot as plt
import csv

authlog = "/var/log/auth.log"
auth_success_dir = "/home/eva/Desktop/tools/task2/authlog_parse/auth_success_logs.csv"
auth_failure_dir = "/home/eva/Desktop/tools/task2/authlog_parse/auth_failure_logs.csv"
privilege_escalation_dir = "/home/eva/Desktop/tools/task2/authlog_parse/privilege_escalation_logs.csv"
attack_tool_keys_dir = "/home/eva/Desktop/tools/task2/authlog_parse/attack_tools_logs.csv"
suspicious_activity_dir = "/home/eva/Desktop/tools/task2/authlog_parse/suspicious_activity_logs.csv"
remote_dir = "/home/eva/Desktop/tools/task2/authlog_parse/remote_logs.csv"



auth_failure_keys = [
    "failed password",
    "invalid user",
    "authentication failure",
    "PAM authentication failure",
    "account locked",
    "excessive authentication failures",
    "invalid login"
]

auth_success_keys = [
    "accepted password",
    "accepted publickey",
    "session opened for user root",
    "root login"
]

privilege_escalation_keys = [
    "sudo",
    "su",
    "useradd",
    "usermod",
    "passwd",
    "account created",
    "deleted user",
    "changed user privileges",
    "possible su attempt"
]

attack_tools_keys = [
    "nmap",
    "hydra",
    "medusa",
    "metasploit",
    "empire",
    "cobaltstrike",
    "mimikatz",
    "powershell",
    "nc",
    "socat",
    "ncat"
]

suspicious_activity_keys = [
    "break-in attempt",
    "refused connect",
    "connection closed by",
    "reverse mapping checking getaddrinfo",
    "port scan",
    "beacon",
    "shell",
    "exploit",
    "c2",
    "implant",
    "dropper",
    "loader",
    "command and control",
    "ransomware",
    "suspicious",
    "anomaly",
    "brute force",
    "privilege escalation",
    "lateral movement"
]

remote_keys = [
    "sshd",          
    "failed password",
    "accepted password",
    "invalid user",
    "connection closed",
    "disconnected",
    "pam_unix",
    "subsystem request for sftp",
]


with open(authlog, 'r') as file:
    for line in file:
        lower_line = line.lower()   # convert to lowercase

        for key in auth_success_keys:
            if key in lower_line:
                with open(auth_success_dir,'a', newline='') as auth_success:
                    writer = csv.writer(auth_success)
                    writer.writerow([line.strip()])
                break

        for key in auth_failure_keys:
            if key in lower_line:
                with open(auth_failure_dir,'a', newline='') as auth_failure:
                    writer = csv.writer(auth_failure)
                    writer.writerow([line.strip()])
                    break
        
        for key in privilege_escalation_keys:
            if key in lower_line:
                with open(privilege_escalation_dir,'a', newline='') as privilege_escalation:
                    writer = csv.writer(privilege_escalation)
                    writer.writerow([line.strip()])
                    break

        for key in attack_tools_keys:
            if key in lower_line:
                with open(attack_tool_keys_dir,'w', newline='') as attack_tools:
                    writer = csv.writer(attack_tools)
                    writer.writerow([line.strip()])
                    break

        for key in suspicious_activity_keys:
            if key in lower_line:
                with open(suspicious_activity_dir, 'w', newline='') as suspicious_activity:
                    writer = csv.writer(suspicious_activity)
                    writer.writerow([line.strip()])
                    break

        for key in remote_keys:
            if key in lower_line:
                with open(remote_dir, 'w', newline='') as remote:
                    writer = csv.writer(remote)
                    writer.writerow([line.strip()])
                    break


        
