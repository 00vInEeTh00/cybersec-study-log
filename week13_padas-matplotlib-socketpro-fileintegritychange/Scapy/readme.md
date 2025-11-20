# Common Host Discovery Methods

Below are **four widely used techniques** to discover active hosts on a network, along with their purpose, advantages, and limitations.

---

## 1. ARP Scan (Address Resolution Protocol)

**What it does:**  
Sends ARP requests within the local subnet and identifies hosts from the ARP replies.

**When to use:**  
- Only works on the **local LAN** (same broadcast domain)  
- Very fast and reliable

**Pros:**  
- Provides **IP ↔ MAC** mapping  
- Very low false-negatives

**Cons:**  
- **Does not work across routers**

---

## 2. ICMP Ping Scan

**What it does:**  
Sends ICMP **Echo Requests** (ping) and waits for **Echo Replies**.

**When to use:**  
- Works on **local and remote networks**, only if ICMP is allowed

**Pros:**  
- Simple  
- Lightweight

**Cons:**  
- Many hosts block or limit ICMP  
- Can cause **false-negatives**

---

## 3. TCP SYN Probe (Half-Open Scan)

**What it does:**  
Sends a TCP **SYN** packet to common ports (22, 80, 443).  
If a host replies with **SYN/ACK**, it is considered alive.

**When to use:**  
- When ICMP is blocked  
- When open TCP ports are likely

**Pros:**  
- Can detect hosts that block ICMP but accept TCP

**Cons:**  
- More intrusive  
- May trigger **IDS/IPS** or get logged

---

## 4. UDP Probe

**What it does:**  
Sends UDP packets to specific ports and infers host presence from:  
- ICMP Port Unreachable  
- Or a valid UDP service response

**When to use:**  
- Useful for networks with UDP-based services

**Pros:**  
- Can identify UDP-only hosts or services

**Cons:**  
- Slow and unreliable  
- High false-negatives  
- Often blocked in networks

---
