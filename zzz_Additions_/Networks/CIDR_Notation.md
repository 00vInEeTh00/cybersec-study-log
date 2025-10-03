# IP Address, Binary Conversion, and CIDR Notes

This note explains **how to convert IP octets to binary**, **calculate CIDR notation**, and **understand subnet masks**, including step-by-step examples.

---

## 1. Understanding Binary Conversion of IP Octets

### Step 1: 8-bit positions

Each octet (0–255) has **8 bits**. Each bit represents a value from left to right:

| Bit 1 | Bit 2 | Bit 3 | Bit 4 | Bit 5 | Bit 6 | Bit 7 | Bit 8 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 128   | 64    | 32    | 16    | 8     | 4     | 2     | 1     |

* Think of each as a **“box” or “switch.”**
* **1 → ON** (we take that value)
* **0 → OFF** (we don’t take that value)

---

### Step 2: Subtraction method (human-friendly)

To convert an octet to binary:

1. Start from the **leftmost bit (128)**
2. Check if it can fit in your number:

   * ✅ Yes → write **1** and subtract the bit value
   * ❌ No → write **0** and do not subtract
3. Move to the next bit value (64 → 32 → … → 1)
4. Repeat until all 8 bits are done

---

### Example: Convert 168 to binary

| Bit Value | Remaining Number | Can we subtract? | Binary |
| --------- | ---------------- | ---------------- | ------ |
| 128       | 168              | Yes ✅            | 1      |
| 64        | 40               | No ❌             | 0      |
| 32        | 40               | Yes ✅            | 1      |
| 16        | 8                | No ❌             | 0      |
| 8         | 8                | Yes ✅            | 1      |
| 4         | 0                | No ❌             | 0      |
| 2         | 0                | No ❌             | 0      |
| 1         | 0                | No ❌             | 0      |

**Result:** `168 → 10101000` ✅

**Tip:** We **skip subtracting** when the bit value is bigger than the remaining number.

---

### Step 3: Convert full IP to binary

Example: **192.168.1.192**

| Octet | Binary   |
| ----- | -------- |
| 192   | 11000000 |
| 168   | 10101000 |
| 1     | 00000001 |
| 192   | 11000000 |

**Full binary IP:** `11000000.10101000.00000001.11000000`

---

### Step 4: Convert Subnet Mask to Binary

Example: **255.255.255.240**

| Octet | Binary   |
| ----- | -------- |
| 255   | 11111111 |
| 255   | 11111111 |
| 255   | 11111111 |
| 240   | 11110000 |

**Full binary subnet mask:** `11111111.11111111.11111111.11110000`

---

### Step 5: Calculate CIDR Notation

* **Count the number of 1s** in the subnet mask
* That number = **CIDR (/n)**

Example:

```
11111111.11111111.11111111.11110000 → 28 ones → /28
```

---

### Step 6: Calculate Number of Usable Hosts

Formula:
[
\text{Usable hosts} = 2^{(32 - \text{CIDR})} - 2
]

Example:

```
/28 → 2^(32-28) - 2 = 2^4 - 2 = 16 - 2 = 14 usable hosts
```

---

### Step 7: Quick Table of Common Subnet Mask Binaries

| Decimal | Binary   |
| ------- | -------- |
| 128     | 10000000 |
| 192     | 11000000 |
| 224     | 11100000 |
| 240     | 11110000 |
| 248     | 11111000 |
| 252     | 11111100 |
| 254     | 11111110 |
| 255     | 11111111 |

**Tip:** Memorize these to quickly identify CIDR and binary without subtraction.

---

## 2. Key Points from Your Doubts

1. **Why we skip subtracting some bit values:**

   * If the remaining number is smaller than the current bit value → we write 0 and move on.

2. **Connection between binary and IP ranges:**

   * **1s in subnet mask** → network part
   * **0s in subnet mask** → host part

3. **Why subtraction works:**

   * Each bit is a “box” with a number.
   * If it fits, take it (1), if not, leave it (0).
   * Builds the binary step by step.

4. **Full IP example for clarity:**

   * IP: 192.168.1.192
   * Binary: `11000000.10101000.00000001.11000000`
   * Subnet: 255.255.255.240 → `/28` → 14 hosts

---

### ✅ Summary

1. Convert each octet to binary using **subtraction method**
2. Convert subnet mask to binary and **count 1s** → CIDR
3. **Usable hosts** = (2^{(32-CIDR)}-2)
4. Memorize **common subnet mask binaries** for speed

This method is **human-friendly**, step-by-step, and covers **all doubts about subtraction, binary, and CIDR**.

---

*End of Notes*
