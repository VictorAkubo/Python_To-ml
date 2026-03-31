import socket

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address_socket = ("localhost",5000)
server_socket.bind(address_socket)

server_socket.listen()

print("server is listening at port 5000")

client_socket, client_address = server_socket.accept()

print(f"connection from {client_address}")



while True:
    msg = client_socket.recv(1024).decode()
    if not msg:
        break
    print("Client says:", msg)
    response = input("Server reply: ")
    client_socket.send(response.encode())

client_socket.close()
server_socket.close()


