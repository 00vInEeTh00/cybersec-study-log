
# 🔐 Linux File Permissions and Security Guide

This guide explains how to understand and manage file permissions and basic security in Linux using common tools: `chmod`, `chown`, and `chgrp`.

---

## 🧩 Understanding File Permissions

Run `ls -l` to see file permissions:

```
-rwxr-xr-- 1 user group 123 Jul 2 08:00 example.sh
```

- `r` = read
- `w` = write
- `x` = execute
- First block: user (owner)
- Second: group
- Third: others

---

## 🛠️ Core Commands

### 📁 `chmod` – Change Permissions

Change numeric permission mode:
```bash
chmod 755 file.sh
```

Symbolic examples:
```bash
chmod u+x file.sh        # Add execute for user
chmod go-w file.txt      # Remove write from group and others
chmod 600 id_rsa         # Read/write for user only (secure private key)
```

### 👤 `chown` – Change Owner

```bash
chown alice file.txt          # Change owner to alice
chown alice:devs file.txt     # Change owner and group
```

### 👥 `chgrp` – Change Group

```bash
chgrp developers file.txt
```

---

## 🛡️ Best Security Practices

| **Action**                            | **Command**                                  |
|----------------------------------------|-----------------------------------------------|
| Make script executable by user         | `chmod u+x script.sh`                         |
| Make a private key secure              | `chmod 600 ~/.ssh/id_rsa`                     |
| Make file read-only for all            | `chmod 444 document.txt`                      |
| Give ownership to user                 | `chown username filename`                     |
| Prevent access to folder from others   | `chmod o-rwx secret_folder/`                  |

---

## 🔎 Example Workflow

```bash
touch secure.txt
chmod 600 secure.txt         # Only owner can read/write
chown bob:staff secure.txt  # Assign to user bob and group staff
ls -l secure.txt
```

Output:
```
-rw------- 1 bob staff 0 Jul 2 10:00 secure.txt
```

---

## 💡 Tips

- Always verify permissions with `ls -l`.
- Use `sudo` if changing files you don’t own.
- Avoid giving `777` permissions unless absolutely necessary.

---
