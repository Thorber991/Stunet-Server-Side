import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

# Sets up the Server Socket for Clients to Connect to.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr): # Every client handling needed from a client connects till he disconnects
    print(f"[SERVER INFO] {addr} Connected")
    
    connected = True
    
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: # Gets the length of the message and decodes it with that bit number when a message is recieved.
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG: # Checks if it's the disconnect message, in which it disconnects the client
                connected = False
                print(f"{addr} disconnected from the Server.")
                print(f"[SERVER INFO] Active Connections: {threading.active_count() -1}")
            
            print(f'[{addr}] {msg}') # Prints the message recieved
            conn.send("Msg Recieved".encode(FORMAT)) # Returns a message to the client
    
    conn.close()


def start(): # Starts the server on the current iPv4 address the server is currently on.
    server.listen()
    print(f'[SERVER INFO] Server is listening on: {SERVER}')
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[SERVER INFO] Active Connections: {threading.active_count() - 1}")

print("[SERVER INFO] server is starting")
start()

