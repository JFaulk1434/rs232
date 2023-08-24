import serial
import socket
import time
import datetime
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")


# Define time between commands
delay = 3

# Define your RS232 parameters
device = config.get("settings", "device")
baudrate = int(config.get("rs232_settings", "baud_rate"))
timeout = int(config.get("rs232_settings", "timeout"))
message = config.get("settings", "message")


# Create serial Connection
ser = serial.Serial(device, baudrate=baudrate, timeout=timeout)


# Define your TCP parameters
ip = config.get("tcp_settings", "ip")
port = config.get("tcp_settings", "port")
buffer = config.get("tcp_settings", "buffer")


def tcp_rs232():
    """Send TCP Command and wait for response on RS232"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message_encoded = message.encode("ascii") + b"\r\n"

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send TCP Message
    start_time = time.time()
    s.send(message.encode)
    print(f"Sent TCP: {message}")

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


if __name__ == "__main__":
    while True:
        tcp_rs232()
        time.sleep(delay)
