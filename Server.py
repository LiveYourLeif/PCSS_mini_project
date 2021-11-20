import socket
import Sorting

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
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = format(message)
    print(f"Score recieved!")

    file = open("saveData.txt", "a")
    file.write(str(clientMsg[2:-1]))
    file.write("\n")
    file.close()
    print("Score saved!")

    bubbleResult = Sorting.Bubble_Sort()
    bubbleResult.sort(Sorting.General_algorithm.value)
    highscore = ({Sorting.Bubble_Sort.value[0]})
    stringify = str(highscore)
    print("Score sorted!")

    scoreString = clientMsg[2:-1]
    highscoreString = stringify[2:-2]

    scores = f"Your score: {scoreString} |" \
             f" Highscore: {highscoreString}"

    newHighscore = f"Your score: {scoreString} |" \
                   f" Highscore: {highscoreString}" \
                   f" | New Highscore!"

    if scoreString < highscoreString:
        bytesToSend = str.encode(newHighscore)
    else:
        bytesToSend = str.encode(scores)

    # Sending a reply to client
    UDPServerSocket.sendto(bytesToSend, address)
