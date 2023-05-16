import telnetlib
import time
import datetime
import configparser

config = configparser.ConfigParser()
config.read("settings.ini")

message = config.get("settings", "message")
login = config.get("telnet_settings", "login")
password = config.get("telnet_settings", "password")

# Define time between commands
delay = 3

# Define your TCP parameters
ip = config.get("telnet_settings", "ip")
port = int(config.get("telnet_settings", "port"))
timeout = int(config.get("telnet_settings", "timeout"))
buffer_size = int(config.get("telnet_settings", "buffer"))


def telnet_cmd():
    """Send Telnet Command and wait for response on Telnet"""
    with telnetlib.Telnet(ip, port, timeout=timeout) as tn:
        tn.set_option_negotiation_callback(lambda *args: telnetlib.DO)
        tn.read_until(b"Password:")
        print("Got password prompt")
        if password:
            tn.write(password.encode("ascii") + b"\n")
            print(f"Sent password: {password}")
            tn.read_until(b"\n")
        if login:
            tn.write(login.encode("ascii") + b"\n")
            print(f"Sent login: {login}")
            tn.read_until(b"\n")
        tn.write(message.encode("ascii") + b"\n")
        print(f"Sent Telnet: {message}")
        data = tn.read_until(b"\n", buffer_size).decode("ascii", errors="ignore")
        print(f"Received Telnet: {data}")
        print("")
        return data


if __name__ == "__main__":
    telnet_cmd()
