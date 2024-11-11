import socket
import threading

# Client settings
HOST = '127.0.0.1'  # IP address of the server (change for remote server)
PORT = 50001        # Port number of the server

# Function to handle receiving messages from the server
def handle_receive(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                print("Server disconnected.")
                break
            print("Server:", data.decode())
    finally:
        client_socket.close()

# Function to handle sending messages to the server
def handle_send(client_socket):
    try:
        while True:
            message = input()
            client_socket.sendall(message.encode())
    finally:
        client_socket.close()

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print("Connected to the server.")

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=handle_receive, args=(client_socket,))
receive_thread.start()

# Start sending messages in the main thread
handle_send(client_socket)

# Wait for the receive thread to finish (in case the connection is closed)
receive_thread.join()

# Close the client socket
client_socket.close()
