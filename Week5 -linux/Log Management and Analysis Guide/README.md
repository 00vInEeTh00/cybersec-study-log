
# 📋 Linux Log Management and Analysis Guide (With Advanced Commands)

This guide covers essential and advanced tools for managing and analyzing log files in Linux. Learn how to inspect, filter, and monitor system logs effectively.

---

## 📁 Important Log Files in `/var/log`

| **Log File**           | **Purpose**                                                              |
|------------------------|--------------------------------------------------------------------------|
| `/var/log/syslog`      | General system activity logs.                                            |
| `/var/log/auth.log`    | Authentication logs (sudo, SSH, login attempts).                         |
| `/var/log/dmesg`       | Kernel boot and hardware-related messages.                               |
| `/var/log/kern.log`    | Detailed kernel logs.                                                    |
| `/var/log/messages`    | General log (Red Hat/CentOS systems).                                    |
| `/var/log/faillog`     | Failed login attempts.                                                   |
| `/var/log/wtmp`        | Binary file storing login/logout history (use `last`).                   |
| `/var/log/btmp`        | Binary file for failed logins (use `lastb`).                             |

---

## 🛠️ Basic Log Analysis Commands

### `tail`
```bash
tail -n 50 /var/log/syslog
tail -f /var/log/syslog
```

### `less`
```bash
less /var/log/auth.log
```

### `cat`
```bash
cat /var/log/dmesg
```

### `grep`
```bash
grep "error" /var/log/syslog
grep "Failed password" /var/log/auth.log
```

### `journalctl`
```bash
journalctl -xe
journalctl -u ssh.service
journalctl --since "1 hour ago"
```

---

## 🚀 Advanced Log Analysis & Monitoring Commands

| **Command**      | **Description**                                                                 |
|------------------|----------------------------------------------------------------------------------|
| `awk`            | Extracts and processes specific fields in logs.                                 |
| `sed`            | Edits log output (e.g., remove timestamps, reformat).                           |
| `watch`          | Runs a command repeatedly at set intervals (e.g., watching logs live).          |
| `logrotate`      | Manages automatic log rotation, compression, and deletion.                      |
| `journalctl`     | Advanced systemd log filtering (by time, service, priority, etc).               |
| `cut`            | Slices out specific columns or sections of logs.                                |
| `zgrep` / `zcat` | Used to search or read compressed log files (e.g., `.log.gz`).                  |
| `multitail`      | View and merge multiple log files at once (color-coded, interactive).           |
| `lnav`           | Log file navigator with SQL-style querying (interactive).                       |
| `ausearch`       | Search logs from audit daemon (`auditd`) for security auditing.                 |
| `last` / `lastb` | View historical logins (from `wtmp`/`btmp`).                                    |

---

## 🔧 Examples of Advanced Usage

### `awk` – Extract Fields
```bash
awk '{print $1, $2, $5}' /var/log/syslog
```

### `sed` – Filter Log Lines
```bash
sed -n '/error/p' /var/log/syslog
```

### `watch` – Monitor Logs
```bash
watch -n 2 tail -n 10 /var/log/syslog
```

### `logrotate`
```bash
sudo logrotate --force /etc/logrotate.conf
```

### `zgrep` / `zcat`
```bash
zgrep "sshd" /var/log/auth.log.1.gz
zcat /var/log/syslog.2.gz | less
```

### `journalctl` (Advanced)
```bash
journalctl --since "2024-07-01" --until "2024-07-02" -p err
journalctl -u apache2.service --no-pager
```

---

## 🧠 Tips

- Use `sudo` when accessing restricted log files.
- Combine `grep`, `awk`, or `cut` for more precise filtering.
- Logs are rotated automatically using `logrotate` on most systems.

---
