import serial
import datetime
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

# Define RS232 parameters
device = "COM11"  # Or Device on MAC: /dev/cu.usbserial-A9UK1ODD
baudrate = 9600
timeout = 1

# Define log file path
log_file_path = "rs232_listener_log.txt"


def listen_to_rs232(device, baudrate, timeout, log_file):
    # Open the log file in write mode to overwrite existing content
    with open(log_file, "w") as file:
        # Create serial Connection
        with serial.Serial(device, baudrate=baudrate, timeout=timeout) as ser:
            file.write(
                f"Starting RS232 listener on {device} with baud rate {baudrate}\n"
            )
            print(f"Starting RS232 listener on {device} with baud rate {baudrate}")

            try:
                while True:
                    # Read data from the RS232 port
                    data = ser.readline()
                    if data:
                        # Get the current timestamp
                        timestamp = datetime.datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        )

                        # Write the received data with the timestamp to the file
                        file.write(
                            f"[{timestamp}] Received data: {data.decode('utf-8', 'ignore')}\n"
                        )
                        print(
                            f"[{timestamp}] Received data: {data.decode('utf-8', 'ignore')}"
                        )

            except KeyboardInterrupt:
                file.write("\nRS232 listener is shutting down.\n")
                print("\nRS232 listener is shutting down.")


# Start listening to RS232
listen_to_rs232(device, baudrate, timeout, log_file_path)
