import os
import socket

# Listening port
serverPort = 1234

# Creating a socket.
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind((socket.gethostname(), serverPort))
serverSock.listen(1)

# Prints out the host name
print("Host Name: ", serverSock.getsockname())

# Accepting the connection.
clientSock, address = serverSock.accept()

# Getting file details.
file_name = input("File Name: ")
file_size = os.path.getsize(file_name)

# Sending file_name and detail.
clientSock.send(file_name.encode())
clientSock.send(str(file_size).encode())

# Opening file and sending data.
with open(file_name, "rb") as file:
    numBytes = 0

    # Running loop while numBytes != file_size.
    while numBytes <= file_size:
        data = file.read(1024)
        if not data:
            break
        clientSock.sendall(data)
        numBytes += len(data)

print("File Transfer Complete.\n")


# Closing the socket.
serverSock.close()

