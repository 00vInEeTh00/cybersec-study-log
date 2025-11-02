
# nftables Firewall Configuration Report

## Overview
This report describes the nftables firewall configuration, explaining each rule, its purpose, and the basic concepts behind nftables, including tables, chains, and rules.

---

## 1. What is nftables?
**nftables** is a modern Linux firewall system that replaces the older iptables framework. It provides better performance, cleaner syntax, and unified handling of both IPv4 and IPv6 through the **inet** family. nftables allows system administrators to filter network traffic, perform NAT, and manage packet flow in a more efficient and organized way.

---

## 2. Key Components of nftables

### **Table**
A **table** is the top-level container that stores chains and rules. It defines the address family (e.g., `ip`, `ip6`, or `inet` for both).  
**Example:**  
`table inet filter` — This table handles both IPv4 and IPv6 traffic for filtering.

### **Chain**
A **chain** is a sequence of rules applied to packets at specific points in the network stack (hooks). Common chains include:
- **input** – handles packets entering the local system.
- **output** – handles packets leaving the system.
- **forward** – handles packets routed through the system.

### **Rule**
A **rule** defines what to do with packets that match certain conditions (e.g., source, port, state). The common actions are `accept`, `drop`, or `reject`.

---

## 3. Current Configuration

### **Table:** `inet filter`
This table filters both IPv4 and IPv6 packets.

#### **Chain: input**
Purpose: Control and protect incoming traffic.

```bash
type filter hook input priority filter; policy drop;
iif "lo" accept
ct state established,related accept
udp dport 53 accept
tcp dport 53 accept
tcp dport { 80, 443 } accept
icmp type echo-request drop
ct state new limit rate 10/second burst 5 packets accept
ct state new drop
ct state invalid drop
```

**Explanation:**
- **policy drop** → Default action is to drop all incoming traffic unless explicitly allowed.  
- **iif "lo" accept** → Allows loopback (local) traffic.  
- **ct state established,related accept** → Accepts packets from already established or related connections.  
- **udp/tcp dport 53 accept** → Allows DNS queries (for name resolution).  
- **tcp dport {80, 443} accept** → Allows HTTP and HTTPS web traffic.  
- **icmp type echo-request drop** → Blocks ping requests for security (prevents discovery).  
- **ct state new limit rate 10/second burst 5 packets accept** → Limits new incoming connections to 10 per second with a burst of 5. Helps prevent DoS attacks.  
- **ct state new drop** → Drops any new connections exceeding the above limit.  
- **ct state invalid drop** → Drops malformed or invalid packets.

#### **Chain: output**
Purpose: Control outgoing traffic from the system.

```bash
type filter hook output priority filter; policy drop;
tcp dport { 53, 80, 443 } accept
udp dport 53 accept
ct state established,related accept
ct state invalid drop
```

**Explanation:**
- **policy drop** → Blocks all outgoing packets unless allowed.  
- **tcp dport {53, 80, 443} accept** → Allows DNS, HTTP, and HTTPS traffic (for browsing websites).  
- **udp dport 53 accept** → Allows DNS queries over UDP.  
- **ct state established,related accept** → Allows packets that are part of established connections.  
- **ct state invalid drop** → Drops corrupted or invalid outgoing packets.

---

## 4. Purpose of This Configuration

This configuration creates a **strict and secure firewall**:
- Blocks all unknown inbound and outbound traffic.
- Allows only essential services (DNS, web browsing).
- Limits connection rates to prevent DoS attacks.
- Blocks ping requests to reduce visibility on the network.
- Ensures only valid traffic passes through.

---

## 5. How Rules Are Formed

To form a rule in nftables, use this syntax:
```bash
sudo nft add rule <family> <table> <chain> <conditions> <action>
```
**Example:**
```bash
sudo nft add rule inet filter input tcp dport 22 accept
```
→ This allows incoming SSH (port 22) connections.

---

## 6. Backup and Restore Configuration

### Backup current ruleset:
```bash
sudo nft list ruleset > ~/nftables-backup.conf
```

### Save as system configuration:
```bash
sudo sh -c 'nft list ruleset > /etc/nftables.conf'
```

### Restore configuration:
```bash
sudo nft -f /etc/nftables.conf
```

---

**✅ Summary:**  
This nftables setup provides a strong baseline firewall configuration, ensuring only necessary traffic (DNS + Web) is permitted while blocking all unwanted connections and limiting new connection rates for better protection.
