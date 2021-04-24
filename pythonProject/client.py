import os
import socket

host = input("Host Name: ")
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverPort = 1234

# Trying to connect to socket.
try:
    clientSock.connect((host, serverPort))
    print("Connected Successfully")
except:
    print("Unable to connect")
    exit(0)

# Send file details.
file_name = clientSock.recv(100).decode()
file_size = clientSock.recv(100).decode()

# Opening and reading file.
with open("./rec/" + file_name, "wb") as file:
    numBytes = 0

    # Running the loop while file is received.
    while numBytes <= int(file_size):
        data = clientSock.recv(1024)
        if not data:
            break
        file.write(data)
        numBytes += len(data)

print("File transfer Complete.")


# Closing the socket.
clientSock.close()
