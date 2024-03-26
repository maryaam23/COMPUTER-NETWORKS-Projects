# Mariam Hamad - 1200837 & Leena Affouri - 1200335 & Nirmeen Alsheikh - 1200200
import socket
import time
def client_program():
    host = "192.168.43.255"  # Broadcast address
    port = 8855  # Server port number
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create UDP socket for server
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    client_socket.settimeout(2)  # Set timeout for receiving response

    student_name = "leena affouri"  # sender's first and last names

    num = 0
    while True:
        message = f"from: {student_name}"  # Message containing student's name
        client_socket.sendto(message.encode(), (host, port))  # Send message to the broadcast address

        try:
            data, address = client_socket.recvfrom(1024)  # Receive response from server
            print(f" {data.decode()} ")

        except socket.timeout:
            print("No response from server")

        num += 1
        time.sleep(2)  # Wait for 2 seconds before sending the next message
    client_socket.close()  # Close the connection

if _name_ == '_main_':
    client_program()