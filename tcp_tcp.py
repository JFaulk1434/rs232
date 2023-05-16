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


if __name__ == "__main__":
    while True:
        tcp_tcp()
        time.sleep(delay)
