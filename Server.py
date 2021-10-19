import socket

server = socket.socket()
print("Socket created")

port = 42069

server.bind(('', port))
server.listen(5)
print("Server is listening")

while True:
    c, addr = server.accept()
    print("Got connection from", addr)
    c.send("Thanks for connecting")
    server
