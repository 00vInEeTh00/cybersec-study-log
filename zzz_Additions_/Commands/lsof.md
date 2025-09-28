# LSOF Command Cheat Sheet

| Command              | Purpose                                         | Example Use                                     |
|---------------------|-------------------------------------------------|------------------------------------------------|
| `lsof`              | Show all open files                             | See everything currently in use               |
| `lsof -i`           | Show network connections (TCP/UDP)             | Check which apps use the network              |
| `lsof -i -nP`       | Show network connections with raw IPs & ports  | Faster and precise, no DNS or service lookup  |
| `lsof -i :8000`     | Show process using a specific port             | Find what’s running on port 8000              |
| `lsof -u eva`       | Show files opened by a user                     | See what files **eva** is using               |
| `lsof /path/to/file`| See which process uses a specific file         | Find who is locking a file                     |
| `lsof -p 1234`      | Show files opened by a specific process ID     | Inspect process **1234**’s activity           |
| `lsof /mnt/usb`     | Show processes using a mount/device            | Useful when unmount says "busy"               |
| `lsof +D /path/dir` | Show all files opened inside a directory       | Track usage in a folder                        |

---

**Notes:**
- `-n` disables hostname resolution.
- `-P` disables port/service name resolution.
- Use `-nP` together for precise IPs and port numbers.
- `lsof` works for files, directories, devices, and network connections.
