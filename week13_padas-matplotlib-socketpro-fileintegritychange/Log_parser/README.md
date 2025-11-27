#Linux Auth Log Analyzer (Suspicious & Privilege Escalation Detection)

This project reads the Linux /var/log/auth.log file, extracts important security-related events, and identifies:

Suspicious authentication attempts

Privilege-escalation related activity

Frequency of repeated commands

Generates CSV output

Produces simple visual graphs for analysis

It helps understand security patterns on your system in a simple automated way.

How It Works (Simple Explanation)

The script reads all lines from /var/log/auth.log.

It extracts:

date

host

process (ex: sudo, sshd, polkitd)

process ID

full log message

It checks whether the line contains suspicious keywords like:
failed password, authentication failure, invalid user, refused, error

It checks for privileged actions using processes like:
sudo, su, pkexec, polkitd, login, sshd, CRON

It counts how many times the same privileged action repeated.

It writes everything into parsed.csv.

Suspicious-only logs are stored in suspicious_logs.csv.

Two graphs are generated:

Privilege Escalation by Process

Suspicious Activity Count by Process

Input File Location

The script analyzes this log:

/var/log/auth.log

Make sure you run the script with root or sudo if needed:

sudo python3 log_parser.py

Output Files

The project automatically generates:

parsed.csv
suspicious_logs.csv
two matplotlib graphs

Requirements

Install Python modules:

pip install pandas matplotlib

What This Project Helps You Identify

Wrong password attempts

Failed sudo access

Invalid user login attempts

Polkit or pkexec privilege attempts

Repeated actions (possible brute-force patterns)

Processes frequently interacting with authentication system
