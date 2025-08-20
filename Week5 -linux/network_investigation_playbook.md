# 🛡️ Network Investigation Playbook (Linux/Ubuntu)

This guide provides **step-by-step instructions** for investigating suspicious processes or connections discovered via `netstat` or `ss` on Linux.

---

## 0) Prep & Preserve
- Create a working folder and log everything (for evidence).
```bash
sudo mkdir -p /root/triage && cd /root/triage
sudo script -a triage_session.log
```
- If actively exfiltrating, block the remote temporarily:
```bash
sudo iptables -I OUTPUT -d x.x.x.x -j DROP
# or: sudo ufw deny out to x.x.x.x
```

---

## 1) Confirm Suspicious Connection
Check sockets with process IDs:
```bash
sudo ss -tupn     # TCP
sudo ss -uanp     # UDP
```
Inspect the process:
```bash
ps -p <PID> -o pid,ppid,user,group,comm,cmd,lstart,etimes
pstree -ap <PID>
readlink -f /proc/<PID>/exe
```

---

## 2) Investigate the Binary
```bash
BIN=$(readlink -f /proc/<PID>/exe)
stat "$BIN"
file "$BIN"
sha256sum "$BIN"
strings -n 8 "$BIN" | head -n 50
dpkg -S "$BIN"   # package ownership?
sudo dpkg -V <pkgname>
```

---

## 3) Capture Volatile Evidence
```bash
T=/root/triage/suspect_<PID> ; sudo mkdir -p "$T"
sudo ss -pant | grep <PID>   | sudo tee "$T/sockets.txt"
sudo lsof -p <PID>           | sudo tee "$T/lsof.txt"
sudo cat /proc/<PID>/cmdline | tr '\0' ' ' | sudo tee "$T/cmdline.txt"
sudo cat /proc/<PID>/environ | tr '\0' '\n' | sudo tee "$T/environ.txt"
sudo ls -l /proc/<PID>/fd    | sudo tee "$T/fd_list.txt"
sudo cp "$BIN" "$T/exe_copy"
```

Optional packet capture:
```bash
sudo timeout 120 tcpdump -nn -s 0 host x.x.x.x -w "$T/peer_capture.pcap"
```

---

## 4) Check Persistence
```bash
systemctl list-unit-files --type=service | grep enabled
sudo grep -R '' /etc/cron* /var/spool/cron
crontab -l
ls -la ~/.config/autostart
cat /etc/ld.so.preload 2>/dev/null
```

---

## 5) Review Logs
```bash
sudo journalctl --since "2 hours ago" | tee "$T/journal_recent.log"
sudo tail -n 500 /var/log/auth.log | tee "$T/auth_tail.log"
sudo last -a | head -n 20
```

---

## 6) Contain Safely
```bash
sudo kill -STOP <PID>    # pause
sudo kill -TERM <PID>    # terminate
sudo kill -KILL <PID>    # force kill
sudo systemctl stop suspicious.service
sudo systemctl disable suspicious.service
```

---

## 7) Hunt for Dropped Files
```bash
sudo find / -xdev -type f -mtime -3 -size -5M -printf '%TY-%Tm-%Td %TH:%TM %p\n' 2>/dev/null | tee "$T/recent_files.txt"
```

---

## 8) Clean Up
- Remove persistence entries
- Reinstall legit packages
- Delete malicious binary (after evidence copy)
- Rotate credentials, keys, and tokens

---

## 9) Harden System
```bash
sudo apt update && sudo apt full-upgrade
sudo ufw enable
sudo apt install fail2ban
```
- Disable password SSH login (use keys only)
- Minimize services at startup

---

## Quick Triage Script
Save as `triage_pid.sh`:
```bash
#!/usr/bin/env bash
PID="$1"; T="/root/triage/suspect_$PID"; mkdir -p "$T"
ss -pant | grep "$PID" | tee "$T/sockets.txt"
lsof -p "$PID" | tee "$T/lsof.txt"
ps -p "$PID" -o pid,ppid,user,group,comm,cmd,lstart,etimes | tee "$T/ps.txt"
pstree -ap "$PID" | tee "$T/pstree.txt"
BIN="$(readlink -f /proc/$PID/exe || true)"
[[ -n "$BIN" && -f "$BIN" ]] && { cp "$BIN" "$T/exe_copy"; sha256sum "$BIN" | tee "$T/bin_hash.txt"; }
```

---

## When to Rebuild Host
- Root compromise
- Kernel-level tricks (`/etc/ld.so.preload` abuse)
- Multiple persistence points

**Steps:**
1. Back up evidence
2. Reinstall from trusted ISO
3. Restore *only data* (not binaries)
4. Rotate all secrets
5. Re-harden system
