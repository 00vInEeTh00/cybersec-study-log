# Nmap Practical Guide — Beginner → Advanced

> Detailed command descriptions, expected outcomes, and notes for each example. Human-friendly and easy to read.

---

## Quick tips before you start

* Many scans need root/administrator privileges (use `sudo`) to send raw packets.
* `-Pn` tells Nmap to skip host discovery and assume the host is up.
* `-sn` (previously `-sP`) performs host discovery only (no port scan).
* Use `-p` to list ports (`-p 22,80,443`) or `-p-` to scan all 65535 TCP ports.
* `--reason` shows why Nmap marked a port state (which packet triggered the decision).

---

# Beginner — learn basic scans (commands, what they do, expected outcomes)

### 1) `nmap -sn 192.168.1.0/24`

**What it does:** Performs host discovery (ping scan) across the specified subnet. No ports are scanned.

**Use:** Quickly find which IPs are online.

**Expected outcome:** A list of IPs that responded. Each listed host will show a short line like `Nmap scan report for 192.168.1.10\nHost is up`.

**Notes:** Uses ICMP, TCP/ACK and/or ARP probes depending on privileges and target type. On local Ethernet, ARP gives the most reliable results.

---

### 2) `nmap 192.168.56.101`

**What it does:** Default Nmap scan against a single IP. Scans the most common 1,000 TCP ports (by default), attempts to guess services.

**Use:** Quick assessment of common open services.

**Expected outcome:** A list of ports and their states (`open`/`closed`/`filtered`) and common service names next to open ports (e.g., `22/tcp open ssh`).

**Notes:** Does not show detailed version info. If you only need a quick look this is a good starting point.

---

### 3) `nmap -p 22,80,443 192.168.56.101`

**What it does:** Scans only the specified ports (22, 80, 443) on the target.

**Use:** Focus on specific services (SSH, HTTP, HTTPS).

**Expected outcome:** For each listed port Nmap reports `open`, `closed`, or `filtered`. Example: `22/tcp open ssh`.

**Notes:** Use commas (no spaces) after `-p`. If you include spaces like `-p 22 80` Nmap treats the next token as a host/target.

---

### 4) `nmap -sV 192.168.56.101`

**What it does:** Performs service/version detection by probing open ports with protocol-specific payloads.

**Use:** Find the software and version (e.g., `OpenSSH 8.2p1`, `nginx 1.18`) running on open ports.

**Expected outcome:** For each open port Nmap will try to identify the service and version. Output shows `SERVICE` and `VERSION` columns.

**Notes:** Slightly noisier and slower than a basic scan but very useful for reconnaissance.

---

### 5) `sudo nmap -O 192.168.56.101`

**What it does:** Attempts OS detection using TCP/IP stack fingerprinting.

**Use:** Guess the operating system (Linux distribution, Windows version) and sometimes device type.

**Expected outcome:** A guessed OS name and accuracy/confidence lines like `OS guesses: Linux 3.10 - 4.11 (98%)` and matched TCP/IP fingerprint entries.

**Notes:** Requires root for sending crafted packets. Accuracy varies — use results as hints, not ground truth.

---

# Intermediate — deeper reconnaissance (commands, what they do, expected outcomes)

### 6) `sudo nmap -sS -p 1-1000 192.168.56.101`

**What it does:** TCP SYN (half-open) scan on ports 1–1000. Sends SYN and reads SYN/ACK (open) or RST (closed).

**Use:** Fast and stealthier than a full connect (`-sT`) because it doesn't complete the TCP handshake.

**Expected outcome:** Ports that respond with `SYN/ACK` are shown as `open`; ports replying `RST` appear `closed`. Filtered ports might show no response.

**Notes:** Requires root for raw sockets. Well-implemented firewalls can detect and log these probes.

---

### 7) `sudo nmap -A 192.168.56.101`

**What it does:** Aggressive scan that combines OS detection (`-O`), version detection (`-sV`), script scanning (`--script=default`), and traceroute.

**Use:** When you want a broad, in-depth inventory in one run (lab only or with permission).

**Expected outcome:** Service versions, script outputs (default scripts), OS guesses, and traceroute hops. Very verbose.

**Notes:** Very noisy and detectable — avoid on targets where stealth matters.

---

### 8) `nmap --script=vuln 192.168.56.101`

**What it does:** Runs NSE (Nmap Scripting Engine) scripts from the `vuln` category against the target.

**Use:** Look for known vulnerabilities and common misconfigurations (in a lab or with permission).

**Expected outcome:** Script output listing potential issues (e.g., `CVE` findings, weak SSL/TLS ciphers, outdated software) or `No vulnerabilities found` messages based on scripts.

**Notes:** Script output quality depends on the target and script accuracy. Some scripts may be slow or intrusive.

---

### 9) `nmap -T3 --fragment 192.168.56.101`

**What it does:** Uses timing template `-T3` (default-ish speed) and fragments packets to split TCP headers across IP fragments.

**Use:** Learn how fragmentation affects IDS/firewall behavior in a controlled lab.

**Expected outcome:** Sometimes improved results against naive packet filters; other times no change. Fragmentation may confuse some middleboxes.

**Notes:** Fragmentation is an evasion technique; results vary with network devices. Use only in a lab.

---

# Advanced — real-world techniques (commands, what they do, expected outcomes)

### 10) `nmap -sA -p 21,22,80,443 103.70.197.78`

**What it does:** ACK scan to determine if a firewall is dropping or allowing probes. Sends TCP ACK packets to the listed ports.

**Use:** Map firewall rules and detect filtered packets (no reply) vs. unfiltered (RST replies).

**Expected outcome:** `unfiltered` if RST is received (host is reachable but port state cannot be determined with ACK); `filtered` if no response or ICMP unreachable.

**Notes:** ACK scans don't tell if ports are open; they help locate packet-filtering devices.

---

### 11) `sudo nmap -D RND:5 192.168.56.101`

**What it does:** Uses random decoys to obfuscate the true source IP in packets sent to the target.

**Use:** Educational/demo only — shows how packets can appear to come from many sources.

**Expected outcome:** Target logs may show multiple source IPs (decoys) plus your real IP; Nmap output remains similar but with decoy info.

**Notes:** Do not use decoys on real-world targets without permission.

---

### 12) `sudo nmap -p- -sV -oA fullscan 192.168.56.101`

**What it does:** Scans all TCP ports (`-p-`), performs version detection, and saves output in three formats: normal `.nmap`, XML `.xml`, and greppable `.gnmap` (`-oA fullscan`).

**Use:** Full inventory and archival of results.

**Expected outcome:** Large list of open ports and services plus saved files `fullscan.nmap`, `fullscan.xml`, and `fullscan.gnmap` in the current directory.

**Notes:** Takes longer; good for comprehensive assessments in a lab.

---

# Interpreting the output you shared (short explanations)

* **`filtered` (no-response):** Nmap did not receive any reply for probes. A firewall or packet filter likely dropped the packets.

* **`open`:** The target replied in a way that indicates a service is listening (e.g., SYN/ACK for TCP).

* **`closed` / `conn-refused`:** The host replied (usually RST), which confirms the host is reachable and the port is closed.

* **`syn-ack` reason:** Shows that Nmap received a SYN/ACK packet, which is why it marked the port `open`.

* **Weird hostnames like `22 (0.0.0.22)`:** Caused by incorrect `-p` syntax (spaces instead of commas). Nmap interpreted tokens as targets. Always use commas in `-p`.

* **`Operation not permitted` on raw sends:** Indicates raw packet sending was blocked. Running as `sudo` or ensuring CAP_NET_RAW capability usually fixes this. Kernel or security settings can prevent raw sockets.

---

# Common mistakes & how to avoid them

* **Wrong `-p` syntax:** `-p 21 22 80` treats `22` and `80` as targets — use `-p 21,22,80`.
* **Missing sudo:** `-sS`, `-O`, and some NSE scripts need root privileges.
* **Confusing hostnames/IPs:** If Nmap prints weird hostnames (like `22 (0.0.0.22)`), double-check your arguments.
* **Assuming OS detection is perfect:** It can be wrong; use as a hint only.

---

# Suggested practice plan (10 quick exercises)

1. `nmap -sn 192.168.1.0/24` — list all up hosts.
2. `nmap -p 22,80,443 192.168.56.101` — check these ports and note states.
3. `sudo nmap -sS -p 1-100 192.168.56.101` — compare speed vs default.
4. `nmap -sV 192.168.56.101` — capture service/version strings.
5. `sudo nmap -O 192.168.56.101` — compare guessed OS to actual VM OS.
6. `nmap --script=http-enum -p80 192.168.56.101` — enumerate web paths.
7. `sudo nmap -A 192.168.56.101` — combined info in one shot.
8. `nmap -sA -p 21,22,80,443 192.168.56.101` — check firewall response.
9. `sudo nmap -p- -sV -oA fullscan 192.168.56.101` — full port sweep and save files.
10. Intentionally run `nmap -p 21 22 80 443 53 192.168.56.101` to see what happens, then correct it to `-p 21,22,80,443,53` and observe difference.

---

## Short glossary

* **open:** port responded and service likely listening.
* **closed:** host replied but port is closed (RST).
* **filtered:** no reply or unreachable — firewall probably blocking.
* **unfiltered:** port is reachable for probes (ACK scan uses this).

---

If you want this exact content exported as a `README.md` or PDF, tell me the format and I'll prepare the file for you.
