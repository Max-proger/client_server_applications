import json
import socket
import sys
import time
import argparse

from common.utils import get_message, send_message
from common.variables import (
    ACCOUNT_NAME,
    ACTION,
    DEFAULT_IP_ADDRESS,
    DEFAULT_PORT,
    ERROR,
    PRESENCE,
    RESPONSE,
    TIME,
    USER,
)
from decor import log


@log
def create_presence(account_name="Guest"):
    out = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {ACCOUNT_NAME: account_name},
    }
    return out


@log
def process_ans(message):
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return "200 : OK"
        return f"400 : {message[ERROR]}"
    raise ValueError


@log
def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    return parser


def main():
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print("В качестве порта может быть указано только число в диапазоне от 1024 до 65535.")
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print("Не удалось декодировать сообщение сервера.")


if __name__ == "__main__":
    main()
