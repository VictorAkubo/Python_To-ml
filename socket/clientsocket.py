import socket

client_socket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server_address = ("localhost",5000)
client_socket.connect(server_address)

while True:
    msg = input("Client says: ")
    client_socket.send(msg.encode())
    response = client_socket.recv(1024).decode()
    print("Server replies:", response)
    

client_socket.close()