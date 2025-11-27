🛡️ File Integrity Monitoring with Jira Alert

This project monitors a directory for any changes in file integrity using SHA-256 hashing.
If a change is detected, the script automatically creates a Jira Incident ticket.

📌 Features

Recursively scans a directory and generates a SHA-256 hash

Compares with the previous hash stored in hash_log.csv

Detects file modifications, additions, or deletions

Automatically creates a Jira Incident when integrity changes

Logs all hashes with timestamps

⚙️ 1. Prerequisites

Install required Python modules:

pip install jira

📁 2. Configure Directory Paths

Update these variables in the script:

file_dir = '/home/eva/Desktop/tools/task3_dir'
hashlog_dir = "/home/eva/Desktop/tools/task3/hash_log.csv"


file_dir → directory to monitor

hashlog_dir → CSV log where previous hashes are stored

🧩 3. Jira Account Configuration

To connect the script with Jira, follow these steps:

✔️ Step 1: Create a Jira Cloud Account

Go to https://www.atlassian.com/software/jira

Sign up or log in

Create a new Jira Software or Jira Service Desk project

Note down the Project Key (e.g., KAN)

✔️ Step 2: Create a Jira API Token

Go to:
https://id.atlassian.com/manage-profile/security/api-tokens

Click Create API token

Give it a name (e.g., "Integrity Monitor")

Copy the token (you will not see it again)

✔️ Step 3: Find Your Jira Cloud Domain

Your Jira URL looks like:

https://yourdomain.atlassian.net


Example:
https://e3630946hash-alert.atlassian.net

✔️ Step 4: Insert Jira Credentials into the Script

Update these fields:

EMAIL = "your_email@example.com"       # Jira login email
API_TOKEN = "your_generated_api_token"
SERVER_URL = "https://yourdomain.atlassian.net"
PROJECT_KEY = "KAN"                    # Your Jira project key
ISSUE_TYPE = "Incident"                # Issue type to create

✔️ Step 5: Install Jira Python Module
pip install jira

🚀 4. Running the Script

Make the script executable (optional):

chmod +x integrity_hash_monitor.py


Run:

python3 integrity_hash_monitor.py

🔎 5. How it Works

The script scans the target directory

It calculates a SHA-256 hash of all files

Compares with last saved hash in hash_log.csv

If different → creates a Jira Incident

Logs the new hash with timestamp

📘 Example Jira Ticket Created

Summary:

Hash Change Detected /home/eva/Desktop/tools/task3_dir


Description:

The file has changed.
Investigation Required.

📄 6. Hash Log Format

hash_log.csv entries:

2025-11-26 18:12:35  a4ffd7c2c6d9...  
2025-11-26 18:14:20  bd99834ac8...  Change_Detected.

🎯 7. Notes / Tips

Ensure Jira Project Key exists

Ensure API Token is valid

Directory must exist before running

CSV log will be created automatically
