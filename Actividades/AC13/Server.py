import socket
from pickle import dumps, loads
from random import randint
from threading import Thread
from time import sleep

DEFAULT_HOST = socket.gethostname()
DEFAULT_PORT = 3338


class Server:

    def __init__(self, host=None, port=None):
        """
        Esta clase representa a un cliente, el cual se conecta
        a un servidor en host:port. Ademas, puede enviar y recibir
        mensajes del servidor
        """
        pass



if __name__ == '__main__':
    server = Server()