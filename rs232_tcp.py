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
MESSAGE = "PWR=1:".encode("ascii")


def rs232_tcp():
    """Send RS232 Command and wait for response on TCP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send RS232 Message
    start_time = time.time()
    ser.write(MESSAGE)
    print(f"Sent RS232: {MESSAGE.decode('ascii')}")

    # Wait for TCP response
    data = s.recv(BUFFER_SIZE)
    data = data.decode("ascii")
    end_time = time.time()

    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received TCP: {data}")
    print(f"Response Time: {response_time:.3f}s")
    print("")


while True:
    rs232_tcp()
    time.sleep(delay)
