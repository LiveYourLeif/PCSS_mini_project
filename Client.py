import socket
import Encounters


playerScore = Encounters.score
file = open("saveData.txt", "a")
file.write(str(playerScore))
file.write("\n")
file.close()

score = f"{playerScore}"

bytesToSend = str.encode(score)


serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)


msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = format(msgFromServer[0])

print(msg[1:])
