import paramiko

ip = "192.168.1.6"
username = "u0_a123"
password = "password"
port = 8022

file = "sample.py"
remote_path = "/data/data/com.termux/files/home/storage/downloads/sample.py"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,username=username,password=password,port=port)

sftp = ssh.open_sftp()
sftp.put(file, remote_path)
sftp.close()

print(f"Uploaded {file} to {remote_path} on termux")

stdin,stdout,stderr = ssh.exec_command(f"cat {remote_path}")

file_content = stdout.read().decode()
print("\n Content of the remote file : ")
print(file_content)
stdin.close()
stdout.close()
stderr.close()
ssh.close()
