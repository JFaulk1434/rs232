import serial
import time
import datetime

# Define time between commands
delay = 3

# Define your RS232 parameters
device = "/dev/ttyUSB0"
baudrate = 115200
timeout = 1

MESSAGE = "PWR=1:"

ser = serial.Serial(device, baudrate=baudrate, timeout=timeout)


def convert_to_hex(string):
    return bytes.fromhex(string)


def rs232_rs232():
    """Send RS232 Command and wait for response on RS232"""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send RS232 Command
    start_time = time.time()
    ser.write(MESSAGE_HEX)
    print(f"Sent RS232: {MESSAGE}")

    # Wait for RS232 response
    data = b""
    while not data:
        data = ser.read(ser.in_waiting)
    end_time = time.time()

    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received RS232: {data}")
    print(f"Response Time: {response_time:.3f}s")
    print("")


MESSAGE_HEX = convert_to_hex(MESSAGE)

while True:
    rs232_rs232()
    time.sleep(delay)
