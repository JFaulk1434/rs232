import socket
import time
import datetime
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

message = config.get("settings", "message")


# Define time between commands
delay = 3

# Define your TCP parameters
ip = config.get("tcp_settings", "ip")
port = int(config.get("tcp_settings", "port"))
buffer = int(config.get("tcp_settings", "buffer"))


def tcp_tcp():
    """Send TCP Command and wait for response on TCP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    message_encoded = message.encode("ascii") + b"\r\n"
    # Send TCP Message
    start_time = time.time()
    s.send(message_encoded)
    print(f"Sent TCP: {message}")

    # Receive TCP Response
    data = s.recv(buffer)
    end_time = time.time()

    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received TCP: {data.decode('Ascii', 'ignore')}")
    print(f"Response Time: {response_time:.3f}s")
    print("")
    time.sleep(delay)


def listen_for_tcp_messages(port=1234):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)

    print(f"Listening on port {port}...")

    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024).decode()
        print(f"Received: {data} from {client_address}")
        client_socket.close()


def listen_for_tcp_messages_with_auth(port=1234, username="admin", password="admin"):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(5)

    print(f"Listening on port {port} with auth...")

    while True:
        client_socket, client_address = server_socket.accept()
        data = client_socket.recv(1024).decode()

        # Fake authentication check
        if data.startswith(f"{username}:{password}"):
            print(f"Authenticated! Received: {data} from {client_address}")
        else:
            print(f"Authentication failed from {client_address}")
            print(f"debug - {data}")

        client_socket.close()


if __name__ == "__main__":
    # Uncomment the one you want to test

    # listen_for_tcp_messages(port=8000)
    listen_for_tcp_messages_with_auth(port=8000, username="admin", password="admin")

    # while True:
    #     tcp_tcp()
