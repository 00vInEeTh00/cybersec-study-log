# 📤 Upload a Python File to Termux using Paramiko

This script lets you:

✅ Connect from your PC to your Android phone (Termux)  
✅ Upload a Python file (like `sample.py`)  
✅ Read the file content on Termux  
✅ And YES — it **replaces the file** if it already exists!

---

## 🧠 What This Script Does

1. Connects to your phone's Termux using **SSH**
2. Sends a Python file using **SFTP**
3. **Replaces the file** if one already exists at the same path ⚠️
4. Reads the file using `cat` command
5. Prints the file content on your PC terminal

---

## ⚙️ Requirements

### 📦 Install These on Your PC:

- Python 3
- `paramiko` library
  ```bash
  pip install paramiko
