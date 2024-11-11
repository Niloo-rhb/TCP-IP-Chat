import socket
import threading

# Server settings
HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 50001      # Port number to listen on

# Function to handle receiving messages from the client
def handle_receive(conn):
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print("Client disconnected.")
                break
            print("Client:", data.decode())
    finally:
        conn.close()

# Function to handle sending messages to the client
def handle_send(conn):
    try:
        while True:
            message = input()
            conn.sendall(message.encode())
    finally:
        conn.close()

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Server is ready to listen on port {PORT}...")

# Accept connection from the client
conn, addr = server_socket.accept()
print(f"Connection established with {addr}")

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=handle_receive, args=(conn,))
receive_thread.start()

# Start sending messages in the main thread
handle_send(conn)

# Wait for the receive thread to finish (in case the connection is closed)
receive_thread.join()

# Close the server socket
server_socket.close()
