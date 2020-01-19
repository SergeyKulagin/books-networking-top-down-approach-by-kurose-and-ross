from socket import *

serverPort = 12001
# welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready")
while True:
    try:
        connectionSocket, addr = serverSocket.accept()
        message = connectionSocket.recv(1024).decode()
        print("Message received: " + message)
        connectionSocket.send(message.upper().encode())
        connectionSocket.close()
    except KeyboardInterrupt:
        print("Close server socket")
        serverSocket.close()
