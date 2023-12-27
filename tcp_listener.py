import socket
from datetime import datetime


def start_tcp_listener(ip, port, log_file):
    # Open the log file in write mode to overwrite existing content
    with open(log_file, "w") as file:
        file.write(f"Starting TCP listener on {ip}:{port}\n")
        print(f"Starting TCP listener on {ip}:{port}")

        # Create a socket object
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Bind the socket to the specified IP address and port
        server_socket.bind((ip, port))

        # Enable the server to accept connections
        server_socket.listen(1)

        try:
            while True:
                # Accept an incoming connection
                client_socket, addr = server_socket.accept()
                connection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{connection_time}] Connection from {addr}\n")
                print(f"[{connection_time}] Connection from {addr}")

                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        break  # If no data is received, break the inner loop

                    # Get the current timestamp
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Write the received byte string with the timestamp to the file
                    file.write(f"[{timestamp}] Received data: {data}\n")
                    print(f"[{timestamp}] Received data: {data}")

                disconnection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"[{disconnection_time}] Disconnection from {addr}\n")
                print(f"[{disconnection_time}] Disconnection from {addr}")

                # Close the client socket
                client_socket.close()

        except KeyboardInterrupt:
            file.write("\nServer is shutting down.\n")
            print("\nServer is shutting down.")

        finally:
            # Close the server socket
            server_socket.close()


# Replace with your machine's IP, the port you want to listen on, and the log file path
ip_address = "0.0.0.0"  # Listen on all available interfaces
port_number = 5001  # Replace with your desired port
log_file_path = "tcp_listener_log.txt"

start_tcp_listener(ip_address, port_number, log_file_path)
