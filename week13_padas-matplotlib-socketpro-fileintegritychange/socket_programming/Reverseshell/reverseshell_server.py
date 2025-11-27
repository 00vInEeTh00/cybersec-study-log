import socket


def server_program():
    #  hostname & port
    host = "0.0.0.0"
    port = 8000  

    server_socket = socket.socket()  # create socket
    
    server_socket.bind((host, port))  # Bind socket to address and port

    # Server can listen 2 clients simultaneously.
    server_socket.listen(2)

    print(f"Server started and listening on port {port}...")
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from:", address)



    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break

        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
