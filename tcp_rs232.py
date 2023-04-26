import serial
import socket
import time
import datetime


# Define time between commands
delay = 3

# Define your RS232 parameters

device = "/dev/ttyUSB0"
baudrate = 115200
timeout = 1

ser = serial.Serial(device, baudrate=baudrate, timeout=timeout)

# Define your TCP parameters
TCP_IP = "10.0.10.66"
TCP_PORT = 5002
BUFFER_SIZE = 1024
MESSAGE = "PWR=1:"


def tcp_rs232():
    """Send TCP Command and wait for response on RS232"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send TCP Message
    start_time = time.time()
    s.send(MESSAGE.encode("Ascii"))
    print(f"Sent TCP: {MESSAGE}")

    # Wait for RS232 response
    data = b""
    while not data:
        data = ser.read(ser.in_waiting)
    data = data.decode("Ascii")
    end_time = time.time()

    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received RS232: {data}")
    print(f"Response Time: {response_time:.3f}s")
    print("")


while True:
    tcp_rs232()
    time.sleep(delay)
