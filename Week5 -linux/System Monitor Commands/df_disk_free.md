
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
