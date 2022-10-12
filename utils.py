"""
AUTHOR:           Marshall Patterson
FILENAME:         utils.py
SPECIFICATION:    Perform different string actions
"""
import os

"""
        NAME:           verify_information
        PARAMETERS:     client_input -> String. Format: # client -s 34.133.93.99 -p 3389 -l log.txt
        PURPOSE:        Verify if client information was correctly entered.
        PRECONDITION:   all parameters are not none and are initialized.
        POST-CONDITION: This instance's fields are initialized to the provided parameters.
"""


def verify_information(client_input: str):
    if input(f"Is the following information correct? {client_input}\n")[0].lower() == 'y':
        return True
    else:
        return verify_information(input("Please enter a new connection... \n"))


"""
            NAME:           parse_ip_info
            PARAMETERS:     client_input -> String. Format: # client -s 34.133.93.99 -p 3389 -l log.txt
            PURPOSE:        Break down user input and return IP and Port.
            PRECONDITION:   all parameters are not none and are initialized.
            POST-CONDITION: This instance's fields are initialized to the provided parameters.
"""


def parse_ip_info(client_input: str, position: int, c1: chr, c2: chr):
    if client_input[position] == c1 and client_input[position - 1] == c2:
        position += 2
        string = ""
        while client_input[position] != ' ':
            string += client_input[position]
            position += 1
        return string

    """
            NAME:           parse_input
            PARAMETERS:     client_input -> String. Format: # client -s 34.133.93.99 -p 3389 -l log.txt
            PURPOSE:        Break down user input and return log file name.
            PRECONDITION:   all parameters are not none and are initialized.
            POST-CONDITION: This instance's fields are initialized to the provided parameters.
    """


def parse_log_file(client_input: str):
    file = []
    completed = 0
    for x in range(1, len(client_input)):
        while not completed:
            if client_input[-x] != ' ':
                file.append(client_input[-x])
                x += 1
            elif client_input[-x] == ' ':
                completed = 1

    return ''.join(file.__reversed__())


"""
            NAME:           parse_input
            PARAMETERS:     client_input -> String. Format: # client -s 34.133.93.99 -p 3389 -l log.txt
            PURPOSE:        Break down user input and return info list in format [IP, PORT, LOGFILE].
            PRECONDITION:   all parameters are not none and are initialized.
            POST-CONDITION: This instance's fields are initialized to the provided parameters.
    """


def parse_input(client_input: str):
    info = []  # [IP, PORT, LOGFILE]
    for x in range(len(client_input)):
        ip = parse_ip_info(client_input, x, 's', '-')
        if ip:
            info.append(ip)
        if info.__len__() == 1:
            port = parse_ip_info(client_input, x, 'p', '-')
            if port:
                info.append(port)
        if info.__len__() == 2:
            file = parse_log_file(client_input)
            if file:
                info.append(file)
    return info


"""
            NAME:           if_file_exists
            PARAMETERS:     file_name (String) -> Name of file
            PURPOSE:        Verify if file exists in project directory.
            PRECONDITION:   all parameters are not none and are initialized.
            POST-CONDITION: This instance's fields are initialized to the provided parameters.
    """


def if_file_exists(file_name: str):
    return os.path.exists(file_name)
