# 🔐 Linux Auth Log Analyzer  
### Suspicious Activity & Privilege Escalation Detector

This project analyzes the Linux **/var/log/auth.log** file and automatically detects:

- Suspicious authentication attempts  
- Privilege-escalation related activity  
- Frequency of repeated commands  
- Generates CSV output  
- Creates simple visual graphs for security analysis  

It helps you understand authentication and privilege behavior on your system in a clean and automated way.

---

## 🛠️ How It Works (Simple Explanation)

The script performs the following steps:

### ✅ 1. Reads `/var/log/auth.log`  
It extracts the following fields from each line:
- **date**
- **host**
- **process** (sudo, sshd, polkitd, login, cron…)
- **process ID**
- **full log message**

---

### ✅ 2. Detects Suspicious Activities  
Looks for keywords such as:

- `failed password`
- `authentication failure`
- `invalid user`
- `refused`
- `error`
- `not valid`

If found → marked as **suspicious = True**

---

### ✅ 3. Detects Privilege Escalation Attempts  
Checks for actions from:

- sudo  
- su  
- pkexec  
- polkitd  
- login  
- sshd  
- CRON  
- systemd-userdbd  
- passwd  

If detected → marked as **privilege_escalation = True**

---

### ✅ 4. Counts Frequency of Repeated Commands  
If the same (user, message) pattern happens multiple times  
→ it increments a **frequency counter**  
Helpful in detecting **brute-force** or repeated sudo attempts.

---

### ✅ 5. Generates Output Files

The script automatically creates:

| File | Description |
|------|-------------|
| **parsed.csv** | All logs with flags + frequency |
| **suspicious_logs.csv** | Only suspicious logs |
| **Graph 1** | Privilege Escalation Events by Process |
| **Graph 2** | Suspicious Activity Count by Process |

---

## 📥 Input File Location

The script analyzes the system log:

