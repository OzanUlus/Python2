import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8"
BYTESİZE = 1024
DİSCONNECT_MESSAGE = "quit"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

server.listen()
print("server çalışıyor...\n")

client_socket, client_address = server.accept()
client_socket.send("server bağlantınız yapıldı.\n".encode(FORMAT))

while True:
    message = client_socket.recv(BYTESİZE).decode(FORMAT)
    if message == DİSCONNECT_MESSAGE:
        client_socket.send("quit".encode(FORMAT))
        print(".ıkış yapıldır...")
        break
    else:
        print(f"{message}\n")
        message = input("mesajınız: ")
        client_socket.send(message.encode(FORMAT))

server.close()