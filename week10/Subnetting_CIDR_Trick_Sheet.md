# 🌐 Subnetting & CIDR Trick Sheet (Beginner Friendly)

This guide helps you quickly calculate **usable hosts**, **block size**, **subnet count**, and **subnet ranges** — all step by step and easy to remember.

---

## 1️⃣ Find Usable Hosts

**Step 1:** Count the **host bits**
```
32 − CIDR = host bits
```
Example: `/28 → 32 − 28 = 4 host bits`

**Step 2:** Apply the formula
```
Usable hosts = 2^(host bits) − 2
```
(We subtract 2 for the network and broadcast addresses.)

✅ **Example:**
```
2^4 − 2 = 14 usable hosts
```

**Shortcut Table:**

| Host Bits | Usable Hosts |
|------------|---------------|
| 1 | 0 |
| 2 | 2 |
| 3 | 6 |
| 4 | 14 |
| 5 | 30 |
| 6 | 62 |
| 7 | 126 |
| 8 | 254 |

---

## 2️⃣ Find Block Size

**Formula:**
```
Block size = 2^(host bits)
```

**Example:**
```
Host bits = 4 → 2^4 = 16
```
🔹 This means each subnet has **16 total addresses** (including network & broadcast).

---

## 3️⃣ Find Subnet Count

**Step 1:** Find **subnet bits**
```
Subnet bits = New prefix − Original prefix
```
**Example:**
```
Original network = 172.16.0.0/16
New subnet = /28 → Subnet bits = 28 − 16 = 12
```

**Step 2:** Apply the formula
```
Number of subnets = 2^(subnet bits)
```
✅ Example: `2^12 = 4096 subnets`

**Shortcut Tip:**  
➡ Smaller prefix (like /28) = More subnets, fewer hosts  
➡ Larger prefix (like /16) = Fewer subnets, more hosts

---

## 4️⃣ Find Subnet Ranges

**Steps:**
1. Start with the network address.  
2. Step size = **block size**  
3. Add the block size to find the next subnet.

**Example (/28 starting from 172.16.5.0):**
```
Network:   172.16.5.0
Usable:    172.16.5.1 – 172.16.5.14
Broadcast: 172.16.5.15
Next Net:  172.16.5.16
```

Repeat by adding +16 (the block size) to get the next subnet.

---

## ✅ Quick Memory Trick

| CIDR | Usable Hosts | Notes |
|------|---------------|--------|
| /30 | 2 | Used for point-to-point links |
| /29 | 6 | Small LANs |
| /28 | 14 | Common for small subnets |
| /27 | 30 | Medium networks |
| /26 | 62 | Larger networks |
| /25 | 126 | Half of a /24 network |

---

### 💡 Summary

| Concept | Depends On | Formula | Example |
|----------|-------------|----------|----------|
| Usable Hosts | Host bits | 2^(host bits) − 2 | /28 → 14 hosts |
| Block Size | Host bits | 2^(host bits) | /28 → 16 addresses |
| Subnet Count | Subnet bits | 2^(subnet bits) | /28 from /16 → 4096 subnets |

---

**Tip to Remember:**  
> **Subnet count** = how many boxes (networks) you made.  
> **Host count** = how many devices fit inside each box.

---
