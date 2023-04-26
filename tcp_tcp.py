import socket
import time
import datetime

# Define time between commands
delay = 3

# Define your TCP parameters
TCP_IP = "10.0.10.66"
TCP_PORT = 5002
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"


def tcp_tcp():
    """Send TCP Command and wait for response on TCP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send TCP Message
    start_time = time.time()
    s.send(MESSAGE.encode("Ascii"))
    print(f"Sent TCP: {MESSAGE}")

    # Receive TCP Response
    data = s.recv(BUFFER_SIZE)
    end_time = time.time()

    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received TCP: {data.decode('Ascii')}")
    print(f"Response Time: {response_time:.3f}s")
    print("")


while True:
    tcp_tcp()
    time.sleep(delay)
