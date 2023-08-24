import serial
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


def rs232_rs232():
    """Send RS232 Command and wait for response on RS232"""
    message_encoded = message.encode("Ascii") + b"\r\n"

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}")

    # Send RS232 Command
    start_time = time.time()
    ser.write(message_encoded)
    print(f"Sent RS232: {message}")

    # Wait for RS232 response
    data = ser.read_until(b"\r\n")
    end_time = time.time()

    if not data:
        print(f"No response received within {timeout}s")
        print("")
        return

    data = data.decode("Ascii").strip()
    # Calculate the response time and print
    response_time = end_time - start_time
    print(f"Received RS232: {data}")
    print(f"Response Time: {response_time:.3f}s")
    print("")


if __name__ == "__main__":
    while True:
        rs232_rs232()
        time.sleep(delay)
