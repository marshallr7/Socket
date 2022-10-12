"""
AUTHOR:           Marshall Patterson
FILENAME:         main.py
SPECIFICATION:    Create and connect a socket to a server.
FOR:              Texas Tech CS 4392-001 Computer Networks
"""
import socket

import utils
import consts

DEBUG = True  # Switch from console input to hard coded fields.


class Socket_Handler:
    """
            NAME:           Socket_Handler.__init__
            PARAMETERS:     ip (String): internet protocol address used for connection,
                            port (String): ip port used for connection.
                            log_file (String): output file for logging information.
            PURPOSE:        This method initializes fields for a new Socket_Handler instance.
            PRECONDITION:   all parameters are not none and are initialized.
            POST-CONDITION: This instance's fields are initialized to the provided parameters.
    """
    def __init__(self, ip: str, port: str, log_file: str):
        self.ip = ip
        self.port = int(port)
        self.log_file = open(f"{log_file}", "w")
        self.s: socket = None

    """
                NAME:           Socket_Handler.log()
                PARAMETERS:     message (String): Message to log to the log file.
                PURPOSE:        This method handles logging of information passed to it.
                PRECONDITION:   all parameters are not none and are initialized.
                POST-CONDITION: This instance's fields are initialized to the provided parameters.
    """
    def log(self, message):
        self.log_file.write(f"{message} \n")
        print(message)

    """
                NAME:           Socket_Handler.create()
                PARAMETERS:     None.
                PURPOSE:        This method creates and assigns our socket.
                PRECONDITION:   IP and Port contain valid connection information for the server.
                POST-CONDITION: None.
    """
    def create(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((self.ip, self.port))
            self.log(f"Connection established on {self.ip}:{self.port}")
        except Exception as e:
            self.log(f"Couldn't connect to server... {str(e)}")
            exit(0)

    """
                NAME:           Socket_Handler.close()
                PARAMETERS:     None.
                PURPOSE:        This method handles closing both the socket and the log file.
                PRECONDITION:   Socket connection is opened
                POST-CONDITION: None.
    """
    def close(self):
        try:
            self.s.close()
            self.log("Socket closed successfully")
            self.log_file.close()
        except Exception as e:
            self.log(f"Error closing connection... {str(e)}")

    """
                NAME:           Socket_Handler.send_message()
                PARAMETERS:     message (String): Message to send to the server.
                PURPOSE:        This method handles passing a message from client to server.
                PRECONDITION:   All parameters are not none and initialized, and the socket is connected to a server.
                POST-CONDITION: None.
    """
    def send_message(self, message: str):
        try:
            self.s.send(message.encode())
            self.log(self.s.recv(1024).decode())
        except Exception as e:
            self.log(f"Error sending message.... {str(e)}")


if __name__ == "__main__":
    if DEBUG:
        s = Socket_Handler(consts.IP, consts.PORT, consts.LOG_FILE)
    else:
        info_string = input("Enter your connection information: \n Please follow the format: client -s 127.168.0.1 "
                            "-p 8080 -l log.txt\n\n")
        utils.verify_information(info_string)
        user_info = utils.parse_input(info_string)
        if not utils.if_file_exists(user_info[2]):
            print("Could not find log file... Using fallback")
            if not utils.if_file_exists(consts.LOG_FILE):
                print(f"Fallback file does not exist... Creating {consts.LOG_FILE}")
                open(consts.LOG_FILE, "x")
            user_info[2] = consts.LOG_FILE
        s = Socket_Handler(user_info[0], user_info[1], user_info[2])
    s.create()
    s.send_message("network")
    s.close()
