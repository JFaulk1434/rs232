import serial
import time
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')


# Define time between commands
delay = 3

# Define your RS232 parameters
device = config.get("settings", "device")
baudrate = int(config.get("rs232_settings", "baud_rate"))
timeout = int(config.get("rs232_settings", "timeout"))
message = config.get('settings', "message")

ser = serial.Serial(device, baudrate=baudrate, timeout=timeout)


if __name__ == "__main__":
    while True:
        data = ser.readline().decode("ascii").strip()
        if data:
            print(f"Received: {data}")
            response = f"{data}\r\n"
            ser.write(response.encode("ascii"))
