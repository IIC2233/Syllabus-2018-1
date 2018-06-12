__author__ = "DQuezadaO & fgbruna"
__credits__ = ["chapito96", "fringlesinthestreet"]

import threading
import socket
import json

HOST = "0.0.0.0"
PORT = 12345

class Server:

    '''
    Esta es la clase encargada de montar el servidor y realizar las operaciones
    lógicas necesarias para el funcionamiento del sistema
    '''

    def __init__(self):
        print("Inicializando servidor...")

    def accept_connections_thread(self):
        '''
        Este método es utilizado en el thread para ir aceptando conexiones de
        manera asíncrona al programa principal
        :return:
        '''
        pass

    def listen_client_thread(self, client_socket):
        '''
        Este método va a ser usado múltiples veces en threads pero cada vez con
        sockets de clientes distintos.
        :param client_socket: objeto socket correspondiente a algún cliente
        :return:
        '''
        pass

    # Los json tiene la forma {'status': % , 'data': %}
    def handle_command(self, received, client_socket):
        '''
        Este método toma lo recibido por el cliente correspondiente al socket pasado
        como argumento.
        :param received: diccionario de la forma: {"status": tipo, "data": información}
        :param client_socket: socket correspondiente al cliente que envió el mensaje
        :return:
        '''

        # Podemos imprimir para verificar que toodo anda bien
        print("Mensaje Recibido: {}".format(received))


    def play_time(self):
        '''
        Esta función decide al ganador. No tiene mucha gracia
        :return:
        '''

        # Se extraen las jugadas
        jug1 = self.jugada["jugador_1"]
        jug2 = self.jugada["jugador_2"]

        # Se reinician los valores
        self.jugada = {"jugador_1": None, "jugador_2": None}


        # Y se ve quién gana
        res = None

        if jug1 == jug2:
            res = "Empate"

        elif jug1 < jug2:
            res = "Jugador2"

        else:
            res = "Jugador1"

        if res == "Empate":
            res_1 = "Empate"
            res_2 = "Empate"
        elif res == "Jugador1":
            res_1 = "Gana"
            res_2 = "Pierde"
        else:
            res_2 = "Gana"
            res_1 = "Pierde"

        # Una vez que se sabe quién gana, se crean 2 mensajes: uno para cada jugador
        msg_jug_1 = {"status": "result",
                     "data": {"eleccion_1": jug1,
                              "eleccion_2": jug2, "res": res_1}}
        msg_jug_2 = {"status": "result",
                     "data": {"eleccion_2": jug1,
                              "eleccion_1": jug2, "res": res_2}}

        # Finalmente, se utiliza la función send para enviar los mensajes
        self.send(msg_jug_1, self.sockets["jugador_1"])
        self.send(msg_jug_2, self.sockets["jugador_2"])

    # Usaremos el método send() para enviar mensajes hacia algún socket cliente.
    # Debemos implementar en este método el protocolo de comunicación donde los
    # primeros 4 bytes indicarán el largo del mensaje.

    @staticmethod
    def send(value, socket):
        '''
        Este método envía la información al cliente correspondiente al socket.
        :param msg: diccionario del tipo {"status": tipo del mensaje, "data": información}
        :param socket: socket del cliente al cual se le enviará el mensaje
        :return:
        '''
        pass

if __name__ == "__main__":


    server = Server()

    # Mantenemos al server corriendo
    while True:
        pass
