# Common Ports Cheat Sheet (Sorted by Daily Use)

## 🏆 Most Familiar / Daily Use
- **22** — SSH (remote login)
- **53** — DNS
- **80** — HTTP
- **443** — HTTPS
- **123** — NTP (time sync)
- **67 / 68** — DHCP (IP assignment)

## 📧 Common but Service-Specific
- **25** — SMTP (mail transfer)
- **110** — POP3 (old mail retrieval)
- **143** — IMAP
- **465 / 587** — SMTP secure / submission
- **993** — IMAPS
- **995** — POP3S

## 💻 Remote Admin / Desktop
- **23** — Telnet (old, insecure, rare)
- **3389** — RDP (Windows remote desktop)
- **5900** — VNC (remote GUI)

## 🗄️ Databases / Backend
- **3306** — MySQL / MariaDB
- **5432** — PostgreSQL
- **1433** — Microsoft SQL Server
- **1521** — Oracle DB
- **6379** — Redis

## 🔧 Networking / Utilities
- **20 / 21** — FTP
- **69** — TFTP (UDP)
- **161 / 162** — SNMP (network monitoring)
- **1080** — SOCKS proxy
- **8000 / 8080** — HTTP alternative / dev servers
- **9000** — Dev tools / admin panels
- **194** — IRC (legacy chat)
- **631** — IPP / CUPS (printing)

---

**Tip:**
- Daily-use ports are normal for most systems.
- Unusual ports may indicate suspicious activity and should be investigated when monitoring with `lsof -i -nP`.
