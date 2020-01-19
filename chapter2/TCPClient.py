from socket import *

serverName = 'localhost'
serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
message = input('Please type a message: ')
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(1024)
print("Modified message: " + modifiedMessage.decode())
clientSocket.close()
