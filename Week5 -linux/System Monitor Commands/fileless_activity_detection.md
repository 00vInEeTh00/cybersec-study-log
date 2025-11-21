# Linux Memory Maps: Deleted File Cheat-Sheet

## 1. Simple Explanation of the Command
sudo cat /proc/*/maps | grep deleted


In simple terms:

It shows all memory regions in running processes that come from files which were deleted.

Linux keeps deleted files in memory as long as a process is still using them, so this command helps you see:
- programs still running from deleted files
- temporary files that were removed but still in use
- shared memory segments that no longer exist on disk
- normal desktop components (Wayland, PipeWire, Chrome) using temporary memfd files
- unusual or suspicious behavior (rare, but important to check)

---

## ✅ 2. What the Output Looks Like

A typical line from `/proc/<pid>/maps` looks like:
7f10ca821000-7f10ca822000 rw-s 00000000 00:01 1068 /memfd:pipewire-memfd:flags=0x0 (deleted)




| Field                        | Meaning                                    |
|------------------------------|--------------------------------------------|
| 7f10ca821000-7f10ca822000    | Memory address range                       |
| rw-s                         | Permissions (read/write/shared)            |
| 00000000                     | File offset                                |
| 00:01                        | Device                                     |
| 1068                         | Inode                                      |
| /memfd:... (deleted)         | Pathname (deleted file backing memory)     |

---

## ✅ 3. How to Analyze and Understand the Output

Here is the safe, clean way to analyze the output without jumping to malware conclusions.

### Step 1 — Identify the Type of Deleted File

Look at the rightmost part of each line.

Common normal cases:

#### 🔹 memfd (normal on desktops)

Examples:
- `/memfd:pipewire-memfd (deleted)`
- `/memfd:wayland-cursor (deleted)`
- `/memfd:mutter-shared (deleted)`

These are normal for:
- PipeWire
- Wayland
- GNOME / KDE
- Chrome / Firefox
- Electron apps

#### 🔹 /dev/shm Chrome/Firefox Memory (normal)
- `/dev/shm/.org.chromium.Chromium.xyz (deleted)`
Also normal.

### Step 2 — Look for Unusual Locations

Unusual if you see deleted files from:
- `/tmp/... (deleted)`
- `/var/tmp/... (deleted)`
- `/dev/shm/<random> (deleted)`
- `/home/user/... (deleted)` when it shouldn’t be deleted
- anon executable memory without names

These are worth inspecting, not necessarily malicious.

### Step 3 — Check the Permissions

Look at the 4-letter field:

| Permissions | Meaning                    |
|-------------|---------------------------|
| r--p        | read-only                  |
| rw-p        | read-write                 |
| r-xp        | executable file            |
| rwxp        | executable + writable (rare, can be suspicious) |

**Important interpretation:**

🟢 Safe examples:
- rw-p
- rw-s
- r--p

🔴 Suspicious examples:
- rwxp (executable + writable)
- r-xp on a deleted file located in /tmp or /dev/shm
- no pathname at all (anonymous) and executable

### Step 4 — Consider the Process That Owns It

You can find the PID by searching:
cat /proc/<PID>/comm




**Examples:**
🟢 Normal processes with deleted memory:
- chrome
- firefox
- pipewire
- gnome-shell
- Xwayland
- systemd
- electron apps

🔴 Unusual processes with deleted memory

Examples that deserve a closer look:
- system daemons (sshd, nginx) with GUI components mapped
- scripts (python, bash) mapping weird memory regions
- unknown binaries
- deleted ELF files mapped into memory from places like /tmp

### Step 5 — Look for Repetition or Abnormal Patterns

Situations worth investigating further:
- rapidly growing number of deleted mappings
- repeated large anonymous regions
- mappings that reappear after reboot
- processes you don’t recognize that keep deleted files open

These patterns indicate misconfiguration, memory bugs, or rarely, suspicious behavior.

---

## ✅ 4. Summary — How to Understand the Output

| What you see                              | What it means                    |
|-------------------------------------------|----------------------------------|
| Many memfd entries                        | Normal Linux desktop behavior    |
| Wayland/PipeWire files (deleted)          | Normal                          |
| Chrome /dev/shm deleted                   | Normal                          |
| Deleted file in /tmp executed             | Unusual → investigate           |
| Executable + writable memory (rwxp)       | Rare → examine process          |
| Anonymous executable memory with (deleted)| Worth checking context          |
| System daemon loading deleted GUI files   | Odd mapping → investigate       |

---







Below is a practical cheat-sheet showing what to grep for, why, and example commands.

---

## ✅ 1. Find Deleted Executables (x permissions and deleted)
These are the highest-risk patterns (possible injected code or hidden binaries).

**Check for executable, deleted mappings**
sudo cat /proc/*/maps | grep 'deleted' | grep 'rwx'


**Check only for executable (x)**
sudo cat /proc/*/maps | grep 'x' | grep deleted




---

## ✅ 2. Find Anonymous Executable Memory (fileless malware)

Anonymous means no filename, often looks like "anon".

sudo cat /proc/*/maps | grep deleted | grep -E 'memfd|anon|memory'


**Narrowed to executable anonymous regions:**
sudo cat /proc/*/maps | grep deleted | grep 'memfd' | grep 'x'





---

## ✅ 3. Search for memfd-created Files (common in fileless attacks)

Normal apps use memfd too, but memfd + executable + deleted = suspicious.

All memfd:
sudo cat /proc/*/maps | grep memfd

memfd that are deleted:
sudo cat /proc/*/maps | grep 'memfd' | grep 'deleted'





---

## ✅ 4. Find Possible Hidden ELF Binaries

If a real binary was mapped but deleted from disk:
sudo cat /proc/*/maps | grep deleted | grep -E '.so|ELF'

Even more direct:
sudo ls -lh /proc/*/exe 2>/dev/null | grep deleted





---

## ✅ 5. Find Deleted /tmp Executables

Attackers often run malware from /tmp then delete it.

sudo cat /proc/*/maps | grep deleted | grep '/tmp'





---

## ✅ 6. Find Deleted Files in /dev/shm

Often used for in-memory payloads:
sudo cat /proc/*/maps | grep deleted | grep '/dev/shm'





---

## ✅ 7. Non-GUI Programs Accessing GUI Files

Example: dconf accessed by a suspicious process.

Find deleted dconf/user:

sudo cat /proc/*/maps | grep deleted | grep dconf





---

## ✅ 8. Look for Growing Repeated Mappings

Memory injection or memory leak:

sudo cat /proc/*/maps | grep deleted | awk '{print $6}' | sort | uniq -c | sort -n


Shows repeated deleted file names and how often they appear.








