# TCP/IP Chat Application

This is a chat application that allows two devices (or instances on the same machine) to communicate with each other using `TCP/IP` protocol in Python. The program consists of two parts: a `Server` and a `Client`. It supports continuous messaging using multithreading, allowing both the server and the client to send and receive messages concurrently.

## Prerequisites

- Python 3.x
- No external libraries are required, as it uses Python’s built-in socket and threading modules.

## Files

- [Server](server.py): The server script that listens for incoming client connections and processes the communication.
- [Client](client.py): The client script that connects to the server and sends/receives messages.

## How to Run

### 1. Server

Run the server script first. This will allow the server to listen for incoming connections from clients.

```bash
python3 server.py
```

### 2. Client

After running the server, run the client script. The client will connect to the server and allow you to send and receive messages.

```bash
python3 client.py
```
