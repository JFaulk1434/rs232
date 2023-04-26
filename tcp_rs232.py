import socket
import time

# IP address and port of the TCP server
ip_address = "10.0.10.66"
port = 5002

# Define the message to be sent
message = ""

message_time = 3 #How many seconds between each message?

while True:
    # Get the current time and format it
    current_time = time.strftime("%H:%M:%S", time.localtime())

    # Construct the message with the timestamp
    message = "PWR ON=1:\n"

    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((ip_address, port))

        # Send the message
        client_socket.sendall(message.encode())

        # Close the socket
        client_socket.close()

        # Wait for 3 seconds
        time.sleep(3)

    except socket.error as err:
        print("Socket error:", err)
        break
