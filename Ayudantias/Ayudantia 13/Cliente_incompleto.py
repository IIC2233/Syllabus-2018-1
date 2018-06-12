__author__ = "DQuezadaO & fgbruna"
__credits__ = ["chapito96", "fringlesinthestreet"]

import threading
import socket
import json
from PyQt5.QtCore import pyqtSignal, QObject
from Ayudantia13_Eventos import ResultadosEvent

HOST = "localhost"
PORT = 12345

class Client(QObject):

    '''
    Esta es la clase encargada de conectarse con el servidor e intercambiar información
    Hereda de QObject con el único motivo de poder emitir y conectar señales.
    Se recomienda que exista un BackEnd aparte del cliente (y que se relacionen).
    '''

    # Señal para avisar cuando llegan resultados del servidor
    trigger_resultados = pyqtSignal(ResultadosEvent)

    def __init__(self):

        # Como heredamos de QObject hay que hacer el llamado a super()
        super().__init__()
        print("Inicializando cliente...")

    def listen_thread(self):
        '''
        Este método es el usado en el thread y la idea es que reciba lo que
        envía el servidor. Implementa el protocolo de agregar los primeros
        4 bytes, que indican el largo del mensaje
        :return:
        '''
        pass

    def handlecommand(self, decoded):
        '''
        Este método toma el mensaje decodificado de la forma:
        {"status": tipo del mensaje, "data": información}
        :param decoded: diccionario con la información
        :return:
        '''

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(decoded))
        

    def send(self, msg):
        '''
        Este método envía la información al servidor. Recibe un mensaje del tipo:
        {"status": tipo del mensaje, "data": información}
        :param msg: diccionario con la información
        :return:
        '''
        pass

    def enviar_jugada(self, event):
        '''
        Este método es el que se gatilla con la señal y manda la información al método send
        :param event: instancia de EleccionBotonEvent con la información
        :return:
        '''

        # Tomamos la información del evento y la pasamos al formato antes descrito
        data = {"status": event.status, "data": event.data}

        # Llamamos al método send para enviar la info al servidor
        self.send(data)


if __name__ == "__main__":

    client = Client()
