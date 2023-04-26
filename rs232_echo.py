import serial
import time

# Define your RS232 parameters
device = "/dev/ttyUSB0"
baudrate = 115200
timeout = 1

ser = serial.Serial(device, baudrate=baudrate, timeout=timeout)

while True:
    data = ser.readline().decode("ascii").strip()
    if data:
        print(f"Received: {data}")
        response = f"{data}\r\n"
        ser.write(response.encode("ascii"))
