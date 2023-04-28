# Requirements

## Purpose

This is a handful of scripts that use RS232 and TCP to test signals. Settings are all located in settings.ini

## Dependencies

- Python 3.x
- PySerial 3.x

## Installation

1. Clone the repository.
2. Install Python 3.x.
3. Install PySerial 3.x by running the command `pip install pyserial` in the terminal/command prompt.

## Usage

1. Connect the Rx/Tx pins of the RS232 port being tested together.
2. Run the script using `python serial_test.py` in the terminal/command prompt.
3. The script will constantly send and receive messages, displaying the time taken for each message in the console.

## Configuration

- Adjust the `port`, `baudrate`, `timeout`, `bytesize`, and `stopbits` parameters in the settings.ini to match the settings of the RS232 connection being tested.

# Find USB to RS232 adapter for PySerial

## Windows

1. Press `Windows + X` keys and select "Device Manager"
2. Look for "Ports (COM & LPT)" and expand it
3. Note the COM port number of your USB to RS232 adapter

## Mac

1. Open "Terminal" application
2. Type `ls /dev/cu.*` and press "Enter"
3. Note the device name of your USB to RS232 adapter (e.g. `/dev/cu.usbserial`)

## Linux

1. Open a terminal window
2. Type `dmesg | grep tty` and press "Enter"
3. Look for the device name of your USB to RS232 adapter (e.g. `/dev/ttyUSB0`)

## Author

# Justin Faulk

## Version

# 1.0
