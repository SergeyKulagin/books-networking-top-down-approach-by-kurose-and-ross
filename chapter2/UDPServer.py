from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("input message: " + message.decode())
    serverSocket.sendto(message.decode().upper().encode(), clientAddress)
