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

ser = serial.Serial(device, baudrate=baudrate, timeout=timeout)

# Define your TCP parameters
ip = config.get("tcp_settings", "ip")
port = config.get("tcp_settings", "port")
buffer = config.get("tcp_settings", "buffer")


def rs232_tcp():
    """Send RS232 Command and wait for response on TCP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))

    message_encoded = message.encode("ascii") + b"\r\n"

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send RS232 Message
    start_time = time.time()
    ser.write(message_encoded)
    print(f"Sent RS232: {message}")

    # Wait for TCP response
    data = s.recv(buffer)
    end_time = time.time()
    data = data.decode("ascii")

    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received TCP: {data}")
    print(f"Response Time: {response_time:.3f}s")
    print("")


if __name__ == "__main__":
    while True:
        rs232_tcp()
        time.sleep(delay)
