import socket
from src import consts
import utils


def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((consts.IP, int(consts.PORT)))
            print("Connection established")
        except Exception as e:
            print(f"Couldn't connect to server... something went wrong {str(e)}")
            print("Exiting...")
            exit(0)


def validate_connection_string():
    print(utils.parse_input(consts.INPUT_STRING))
