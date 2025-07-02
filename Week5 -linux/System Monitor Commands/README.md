
# 🖥️ Linux System Monitoring Guide

This guide explains essential and advanced tools for monitoring system performance on Linux. Use these commands to track CPU, memory, disk usage, and other critical metrics.

---

## 🧰 Core Monitoring Commands

| **Command**     | **Purpose**                                      |
|------------------|--------------------------------------------------|
| `uptime`        | Shows system uptime and load averages.           |
| `top`           | Displays real-time CPU, memory, and process usage. |
| `df -h`         | Displays disk space usage.                       |
| `du -sh /path`  | Shows the size of a specific folder or file.     |
| `free -h`       | Displays RAM and swap usage.                     |
| `vmstat 1 5`    | Shows performance metrics like CPU, memory, and I/O. |

---

## 🧪 Example Script: `sys_monitor.sh`

```bash
#!/bin/bash

echo "===== SYSTEM MONITORING REPORT ====="

echo "1. Uptime:"
uptime
echo

echo "2. CPU & Memory Usage (top):"
top -b -n 1 | head -n 10
echo

echo "3. Disk Usage (df -h):"
df -h
echo

echo "4. Folder Size (/var/log):"
du -sh /var/log 2>/dev/null
echo

echo "5. RAM Usage (free -h):"
free -h
echo

echo "6. Performance Stats (vmstat):"
vmstat 1 5
echo

echo "===== END OF REPORT ====="
```

---

## ⚙️ How to Use the Script

```bash
chmod +x sys_monitor.sh
./sys_monitor.sh
```

To save the output:
```bash
./sys_monitor.sh > system_report.txt
```

---

## 📂 Sample Output

```
Uptime: 08:58:28 up 13 min,  1 user,  load average: 0.43, 0.45, 0.29
CPU: 1.1% used, 97.8% idle
Memory: 4.8 GiB used, 783 MiB free
Disk: /dev/nvme0n1p2 - 10% used
Logs: /var/log - 679 MB
```

---

## 🛠️ Optional / Advanced Tools (But Very Useful)

These tools offer more detailed or interactive system monitoring:

| **Tool**     | **Description**                                     | **Install (Ubuntu/Debian)**     |
|--------------|------------------------------------------------------|----------------------------------|
| `htop`       | Interactive system monitor (better than `top`)       | `sudo apt install htop`          |
| `iotop`      | Real-time disk I/O per process                       | `sudo apt install iotop`         |
| `iostat`     | CPU and disk throughput stats (`sysstat` package)    | `sudo apt install sysstat`       |
| `glances`    | Full monitoring dashboard (web + CLI)                | `sudo apt install glances`       |
| `sar`        | Collects and displays historical performance data    | `sudo apt install sysstat`       |
| `nmon`       | Performance monitoring tool with charts              | `sudo apt install nmon`          |
| `dstat`      | Replaces vmstat, iostat, and ifstat with one tool    | `sudo apt install dstat`         |

---

## 🧠 Pro Tips

- Use `sudo` for accurate disk usage and log checks.
- Automate the script with a `cron` job for regular health monitoring.
- Redirect logs to files for system audits:
  ```bash
  ./sys_monitor.sh >> ~/monitor_logs/system_$(date +%F).log
  ```
