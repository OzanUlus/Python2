import socket

PORT = 12345
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER,PORT)
FORMAT = "utf-8"
BYTESİZE = 1024
DİSCONNECT_MESSAGE = "quit"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDRESS)

while True:
    message = client.recv(BYTESİZE).decode(FORMAT)
    if message == DİSCONNECT_MESSAGE:
        client.send("quit".encode(FORMAT))
        print(".ıkış yapılıyor...")
        break
    else:
        print(f"{message}\n")
        message = input("mesajınız: ")
        client.send(message.encode(FORMAT))

client.close()
