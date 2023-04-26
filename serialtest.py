import serial
import time
import datetime

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
count = 0

while True:
    # Send message and get time
    send_time = time.monotonic()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    ser.write(f"{timestamp} | Hello from Linux\r\n".encode("Ascii"))
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
    time.sleep(3)
    count += 1
