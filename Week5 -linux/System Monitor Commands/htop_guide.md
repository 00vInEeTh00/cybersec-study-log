
# 📊 `htop` in Linux — System Monitor (Beginner Friendly)

---

## 🧠 What is `htop`?

`htop` is an interactive and colorful system monitor for Linux.  
It shows **CPU**, **memory**, and **running processes** — in real-time!

> ✅ It's like a more friendly and visual version of `top`.

---

## 🔧 How to Install

```bash
sudo apt update
sudo apt install htop
```

Run it with:

```bash
htop
```

---

## 🖥️ `htop` Screen Breakdown

### 🟪 CPU Usage (Cores/Threads)

```
0[||||      ]  7.5%
1[||        ]  4.4%
...
7[|||       ]  1.9%
```

- Each row shows one **CPU thread**.
- Since your processor has:
  - **4 cores** × **2 threads per core** = **8 threads**
- That’s why `htop` shows `0` to `7`.

**Color meanings**:
- 🟥 Red = Kernel (system)
- 🟩 Green = User apps
- 🟦 Blue = Nice (low priority)
- 🟧 Orange = I/O wait

---

### 🧠 Memory and Swap

```
Mem[|||||||||||||||||||||||||||     ]  3.39G/7.50G  
Swp[||||||||||||||||||             ]  2.05G/4.00G
```

- **Mem** = RAM (fast memory)
- **Swp** = Swap (slow, on disk)
- Shows usage as bar and number

💡 High swap usage can mean low RAM or memory-heavy apps.

---

### 🔩 Tasks & Load Average

```
Tasks: 155, 1035 thr, 156 kthr; 1 running  
Load average: 0.81 0.85 0.65  
Uptime: 1 day, 02:06:58
```

- **Tasks** = Total processes  
- **thr** = Threads  
- **kthr** = Kernel threads  
- **Load avg** = How busy the system is over 1, 5, and 15 mins  
- **Uptime** = How long the system is running

---

## 🔤 Process Table Columns

| Column  | Meaning                        |
|---------|--------------------------------|
| `PID`   | Process ID                     |
| `USER`  | Who owns the process           |
| `PRI`   | Priority                       |
| `NI`    | Niceness (affects priority)    |
| `VIRT`  | Virtual memory (total address space) |
| `RES`   | Resident memory (actual RAM used)    |
| `SHR`   | Shared memory                  |
| `CPU%`  | CPU usage                      |
| `MEM%`  | Memory usage                   |
| `TIME+` | Total CPU time used            |
| `COMMAND` | Name of the process          |

---

## 🎹 Keyboard Shortcuts in `htop`

| Key  | Action                         |
|------|--------------------------------|
| `↑ ↓` | Navigate process list         |
| `F3` | Search                         |
| `F4` | Filter                         |
| `F5` | Tree view                      |
| `F6` | Sort column                    |
| `F9` | Kill process                   |
| `F10`| Quit `htop`                    |

---

## 💡 Extra Tip: Check Real Cores

To see real vs. logical CPUs:

```bash
lscpu
```

Example output:

```
CPU(s):              8
Thread(s) per core:  2
Core(s) per socket:  4
```

This means:
- You have 4 physical cores
- 8 logical CPUs (threads)

---

## 🧠 Memory Trick:

> If `top` is the math version of a monitor 📊,  
> then `htop` is the comic book version 🎨 — same data, way more fun!
