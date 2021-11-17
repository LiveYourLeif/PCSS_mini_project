import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams

while True:
    try:
        serverCommand = int(input())
        if serverCommand == 0:
            print("test")
    except EOFError:
        break

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = format(message)
    print(clientMsg[2:-1])

    msgFromServer = f"Your Highscore: {clientMsg[2:-1]}"

    bytesToSend = str.encode(msgFromServer)
    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
