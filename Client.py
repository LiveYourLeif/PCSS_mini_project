import socket
import Encounters

playerScore = Encounters.score
score = f"{playerScore}"

scoreToSend = str.encode(score)

serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(scoreToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = format(msgFromServer)

print(msg[3:-24])
