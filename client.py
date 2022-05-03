import socket

HEADER = 64
PORT = 5050
SERVER = input()
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

# Sets up the Client Connection to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg): # Allows the client to send a message to the server.
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message) 
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length: # Gets the length of the message and decodes it with that bit number when a message is recieved.
        msg_length = int(msg_length)
        msg = client.recv(msg_length).decode(FORMAT)

        print(f'[{addr}] {msg}')

# Test messages sent to Server
send("Hello World!")
input()
send("Hey Byddy!")
input()
send("Hello Budds")
input()
send(DISCONNECT_MSG)
input()
send("Have Fun!")
input()
