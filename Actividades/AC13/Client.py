import socket
from pickle import dumps, loads
import sys
from threading import Thread
from time import sleep
from ventana_principal import MiVentana, QApplication

DEFAULT_HOST = socket.gethostname()
DEFAULT_PORT = 3338


class Client:

    def __init__(self, host=None, port=None):
        """
        Esta clase representa a un cliente, el cual se conecta 
        a un servidor en host:port. Ademas, puede enviar y recibir 
        mensajes del servidor
        """
        self.ventana = MiVentana(self.pedir_mover, self.desconectar)

    def pedir_mover(self, x, y):
        """
        Esta función se llama cada vez que se aprieta una tecla, entregando la
        posición x, y a la que se deberia mover. En este paso deberían enviarle
        un mensaje al servidor indicando que se quiere mover el personaje a la
        posición x, y
        """
        print(x, y)

    def desconectar(self):
        """
        Esta función se llama cuando se cierra la interfaz. En este paso
        deberían enviarle un mensaje al servidor indicando que se van a
        desconectar y manejar la desconexion del cliente.
        """
        pass



if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)
    sys.__excepthook__ = hook
    app = QApplication([])
    client = Client()
    app.exec_()
