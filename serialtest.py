"""
This is a small script to constantly send RS232 messages while at the same time receiving them. 
Ideally at the end of the RS232 connection you would connect the Rx/Tx together so the message goes through the devices,
and then returns. This allows the program to time how long it took for the message to be sent down the line and come back.
"""


import serial
import time
import datetime

# Adjust as needed
port = "COM1"  # See readme.md depends on OS program is run on
baudrate = 9600
timeout = 1
bytesize = 8
stopbits = serial.STOPBITS_ONE


# Create Serial Instance
ser = serial.Serial(
    port=port, baudrate=baudrate, timeout=timeout, bytesize=bytesize, stopbits=stopbits
)


while True:
    # Send message and get time
    send_time = time.monotonic()
    ser.write(f"Hello World!!!\r\n".encode("Ascii"))
    ser.flush()

    # Receive message and calculate time taken
    receive_time = time.monotonic()
    message = ser.readline()
    if message:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        receive_time = time.monotonic()
        time_taken = receive_time - send_time
        print(
            f"{timestamp} | Time taken: {time_taken:.3f}s | Received:",
            message.decode("Ascii"),
        )

    # Wait for 1 second before sending next message
    time.sleep(1)
