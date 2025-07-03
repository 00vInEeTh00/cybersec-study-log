
# 🛡️ `df` Command in Cybersecurity

---

## 🧠 What is the role of `df` in Cybersecurity?

> `df` helps security professionals **check disk space usage** — this is important because attackers, malware, or system issues can **fill the disk**, which causes **security risks and crashes** 😱

---

## 🧱 Why Disk Space is Important in Security?

If your disk gets full:

- 🔐 System **can’t log** security events (logs get lost)
- 📦 Backups may **fail silently**
- 🧨 System may **crash or freeze**
- 🧠 Attackers may **fill your disk** on purpose (called **DoS attack**)

---

## 📊 How `df` Helps in Cybersecurity (Use Cases)

---

### 🕵️‍♂️ A. Detecting Abnormal Disk Usage

```bash
df -h
```

**Use it to:**
- Look for partitions (like `/`, `/var`, or `/home`) that are **almost full**
- Example: If `/var` is 100% full → **logs can’t be written**
- Could be a **sign of malware**, log flooding, or failed cleanup

---

### 📁 B. Monitoring `/tmp` or `/var/tmp`

```bash
df -h /tmp
df -h /var/tmp
```

- Hackers might store large **malware** or **stolen data** here
- If `/tmp` is suddenly huge → suspicious!

---

### 🔥 C. Protecting Against "Disk Filling" Attacks (DoS)

Bad actors may:
- Fill up your disk with junk files
- Crash the system or block logging

Use this to keep watch:

```bash
watch -n 60 df -h
```

Monitors disk every 60 seconds.

---

### 📜 D. Checking `/var/log` for Log Storage

Logs = heart of system auditing ❤️

If `/var` or `/var/log` fills up:
- Logs stop recording ❌
- You lose track of what happened!

```bash
df -h /var
```

💡 Tip: Set alerts if usage goes above 80–90%

---

## 🧠 Summary Table

| Use Case                              | Why it's important in security       |
|---------------------------------------|--------------------------------------|
| Monitor disk space                    | Prevent crashes, log loss, DoS       |
| Detect full `/tmp` or `/var/tmp`     | Spot malware or hidden data          |
| Watch `/var/log` disk                 | Ensure logs are always recorded      |
| Detect abnormal usage patterns        | Catch suspicious or hacked behavior  |

---

## 🔍 Bonus Tip — Combine with `du`

To find **which folder** is taking space:

```bash
du -sh /*
```

Then investigate large folders like `/var`, `/tmp`, or `/home`.

---

## 🧠 Memory Trick

> `df` = Disk Full? = Danger Found! 🧨  
> Use it daily like a security camera for your disk 👁️💽





⚠️ Important Note

    df shows total disk usage

    It can’t tell you the file names

    For that, you need extra tools 👇



# 📦 Monitoring Downloads & Uploads in Linux (Disk Activity Tools)

---

## 🎯 Goal

Learn how to **watch disk space changes** and **see what’s being downloaded or uploaded** — live and clearly! 👁️💽

---

## 🛠️ 1. `df` — Disk Free

### ✅ Use:
Check **total disk space** changes (grows when files are downloaded).

### Example:
```bash
watch -n 5 df -h
```

> Runs `df -h` every 5 seconds.  
> If `Used` increases, a file is being downloaded or created!

---

## 🧮 2. `du` — Disk Usage (per folder)

### ✅ Use:
Check how much space a **specific folder** (like Downloads) is using.

### Example:
```bash
watch -n 5 du -sh ~/Downloads
```

> Shows how much space your `Downloads` folder is using — updates every 5 seconds.

---

## 🔍 3. `lsof` — List of Open Files

### ✅ Use:
See **what files are open or being accessed**.

### Example:
```bash
lsof +D ~/Downloads
```

> Lists all currently open files in the `Downloads` folder.

---

## 🔥 4. `iotop` — Live Disk I/O Monitor

### ✅ Use:
See which **process is reading or writing** to disk **right now**.

### Example:
```bash
sudo iotop
```

> Like `top`, but for disk usage.  
> Shows **which apps are downloading or writing**.

---

## 📈 5. `inotifywait` — Watch for File Changes

### ✅ Use:
Live-monitor if a file is **created, changed, or deleted**.

### Example:
```bash
inotifywait -m ~/Downloads
```

> Prints a message every time something changes in `Downloads`!

> Requires: `sudo apt install inotify-tools`

---

## 🧠 Summary Table

| Tool        | What it does                           | Best for                            |
|-------------|----------------------------------------|--------------------------------------|
| `df -h`     | Shows total disk space usage           | Big changes in system               |
| `du -sh`    | Shows folder-level disk usage          | Watching one folder like Downloads  |
| `lsof +D`   | Lists open files in folder             | See files currently in use          |
| `iotop`     | Shows live disk-writing processes      | Know who is writing to disk now     |
| `inotifywait` | Alerts when files are created/changed | File activity in real-time          |

---

## 🧠 Memory Trick

> - `df` = "Did Files grow?" 📦  
> - `du` = "Details of Usage" 🧮  
> - `lsof` = "List Stuff Opened" 🔎  
> - `iotop` = "I/O Live Monitor" 🔥  
> - `inotifywait` = "Instant File Alert" ⏰

---

Happy Monitoring! 🖥️🧠🔐



