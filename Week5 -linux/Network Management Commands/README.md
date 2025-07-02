
# 🌐 Linux Network Management Commands

This guide explains essential network management commands used to troubleshoot and manage network connections on Linux systems.

---

## 🧰 Core Network Commands

| **Command**     | **Purpose**                                            |
|------------------|--------------------------------------------------------|
| `ifconfig`      | Displays network interface details (legacy tool).      |
| `ip a`          | Shows all IP addresses and interfaces (modern tool).   |
| `ping`          | Tests network connectivity to another host.            |
| `netstat -tuln` | Lists open ports and listening services (deprecated).  |
| `ss -tuln`      | Shows open ports and connections (preferred over netstat). |
| `traceroute`    | Traces route packets take to a destination.            |
| `nmap`          | Scans hosts/networks for open ports and services.      |

---

## 🔍 Command Examples and Outputs

### `ifconfig`
```bash
ifconfig
```
Shows IP address, MAC address, and network status for interfaces.

---

### `ip a`
```bash
ip a
```
Modern replacement for ifconfig, provides detailed IP and interface info.

---

### `ping`
```bash
ping google.com
```
Checks if a remote host is reachable.

---

### `netstat`
```bash
netstat -tuln
```
Lists TCP/UDP ports and services (use `ss` instead if not installed).

---

### `ss`
```bash
ss -tuln
```
Shows socket statistics and listening ports (more modern than netstat).

---

### `traceroute`
```bash
traceroute google.com
```
Displays each hop between your machine and a target host.

---

### `nmap`
```bash
nmap -sS 192.168.1.1
```
Performs a TCP SYN scan to check open ports on a target IP.

---

## 💡 Tips

- Use `sudo` if some commands don’t return complete data.
- Combine tools (`ping`, `traceroute`, `ss`) for better diagnostics.
- Use `nmap` responsibly — only scan systems you own or have permission to scan.

---
