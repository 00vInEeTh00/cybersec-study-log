# Linux Network Monitoring Commands Cheat Sheet (Ranked)

## 1️⃣ Most Advanced & Effective

- **`ss`**
  - Modern replacement for `netstat`
  - Fast, shows sockets + processes, supports filtering (TCP/UDP, ports, states)
  - Example:
    ```bash
    ss -tuln      # listening TCP/UDP ports
    ss -ant       # all TCP connections
    ss -p         # show process using socket
    ```

- **`lsof -i`**
  - Shows which process uses which network port/IP
  - Crucial for security and troubleshooting
  - Example:
    ```bash
    lsof -i -nP   # list all network connections with IP & port numbers
    lsof -i :80   # check which process uses port 80
    ```

- **`tcpdump`**
  - Captures raw packets for deep network analysis
  - Requires understanding of protocols
  - Example:
    ```bash
    sudo tcpdump -i eth0          # capture packets on interface eth0
    sudo tcpdump -i eth0 port 80  # capture only HTTP traffic
    ```

- **`nethogs`**
  - Monitors bandwidth used by each process
  - Example:
    ```bash
    sudo nethogs                 # interactive bandwidth per process
    ```

## 2️⃣ Common & Useful

- **`iftop`**
  - Real-time traffic monitoring per host
  - Example:
    ```bash
    sudo iftop -i eth0
    ```

- **`ping` / `traceroute`**
  - Connectivity & routing checks
  - Examples:
    ```bash
    ping google.com
    traceroute google.com
    ```

- **`dig` / `nslookup`**
  - DNS query and debugging
  - Examples:
    ```bash
    dig google.com
    nslookup 8.8.8.8
    ```

- **`curl` / `wget`**
  - Test HTTP/HTTPS connectivity
  - Examples:
    ```bash
    curl -I https://example.com
    wget https://example.com
    ```

- **`netstat`**
  - Old tool for showing connections and routing tables
  - Replaced largely by `ss`
  - Example:
    ```bash
    netstat -tuln
    ```

## ✅ Summary Table (Advanced → Basic)

| Rank | Command        | Use Case / Why |
|------|----------------|----------------|
| 1    | `ss`           | Fast, modern, shows sockets + processes |
| 2    | `lsof -i`      | Process → port → IP mapping, security monitoring |
| 3    | `tcpdump`      | Packet capture, deep network analysis |
| 4    | `nethogs`      | Bandwidth per process, real-time monitoring |
| 5    | `iftop`        | Host-based traffic monitoring |
| 6    | `ping` / `traceroute` | Connectivity & routing checks |
| 7    | `dig` / `nslookup`    | DNS analysis |
| 8    | `curl` / `wget`       | HTTP/HTTPS connectivity testing |
| 9    | `netstat`      | Old, basic connection monitoring |

---

**Tip:**
- Use **`ss` and `lsof -i`** for modern network monitoring and security checks.
- Use **`tcpdump` and `nethogs`** for deeper traffic inspection.
- Support commands (`ping`, `dig`, `curl`) help diagnose connectivity issues.
