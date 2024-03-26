# Mariam Hamad - 1200837  & Leena Affouri - 1200335 & Nirmeen Alsheikh - 1200200
import socket
import time
def server_program():         #define server
    host = "192.168.43.246"   # IPv4 Address for server.
    port = 8855               # port number.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creat UDP socket.
    server_socket.bind((host, port)) # bind socket to local port number.
    clients = {}  # dictionary to store client information
    # Add server name
    server_first_name = "Mariam"
    server_last_name = "Hamad"
    print(f"Server Name: {server_first_name} {server_last_name}")
    while True:
        message, client_address = server_socket.recvfrom(1024) # read from UDP socket into message,getting client address
                                                               # client address = client ip & port number.
        message = message.decode()
        current_time = time.strftime("%H:%M:%S", time.localtime())
        if client_address not in clients:
            # New client
            clients[client_address] = message
        else:
            # Existing client, update the message and time
            clients[client_address] = (message, current_time)
            print(f"Received message from {message} at {current_time}")
            # Send acknowledgment to client
            response_message = f"Server received your message at {current_time}"
            server_socket.sendto(response_message.encode(), client_address)
if __name__ == "__main__":
    server_program()
