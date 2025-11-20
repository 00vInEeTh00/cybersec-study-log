# Important Ubuntu Security Logs

Below is a list of **Ubuntu-specific log files** commonly used for analyzing security incidents.

---

## 1. `/var/log/auth.log`
Tracks all authentication-related activity.  
**Use:** Logins, failed logins, sudo usage, SSH attempts, brute-force detection.

---

## 2. `/var/log/syslog`
General system log storing system-wide events.  
**Use:** Service errors, system warnings, suspicious behavior, kernel notices.

---

## 3. `/var/log/kern.log`
Kernel-level messages.  
**Use:** Hardware issues, kernel errors, possible rootkit-related activity.

---

## 4. `/var/log/dmesg`
Boot-time and kernel ring buffer messages.  
**Use:** Detect unusual hardware or boot behavior.

---

## 5. `/var/log/faillog`
Records failed login attempts.  
**Use:** Identify brute-force attempts.

---

## 6. `/var/log/btmp` (binary)
Stores failed login attempts in binary format.  
**View using:** `lastb`  
**Use:** Find repeated or suspicious login failures.

---

## 7. `/var/log/wtmp` (binary)
Tracks successful logins and logouts.  
**View using:** `last`  
**Use:** Monitor who logged in and when.

---

## 8. `/var/log/lastlog`
Shows the last login for each user.  
**Use:** Detect unexpected or unknown login activity.

---

## 9. `/var/log/apt/history.log`
Records package installation and updates.  
**Use:** Check for unauthorized or suspicious software installation.

---

## 10. `/var/log/apt/term.log`
Detailed output of APT operations.  
**Use:** Inspect installation and update details.

---

## 11. `/var/log/ufw.log`
Logs from Ubuntu's firewall (UFW).  
**Use:** Blocked/allowed traffic and suspicious connection attempts.

---

## 12. `/var/log/audit/audit.log` (if auditd enabled)
Linux audit system logs.  
**Use:** Permission denials, system calls, policy violations (AppArmor/SELinux).

---
