__author__ = "DQuezadaO & fgbruna"
__credits__ = ["chapito96", "fringlesinthestreet"]

import threading
import socket
import json


class Server:

    '''
    Esta es la clase encargada de montar el servidor y realizar las operaciones
    lógicas necesarias para el funcionamiento del sistema
    '''

    def __init__(self):
        print("Inicializando servidor...")

        # Ponemos la dirección donde va a estar situado nuestro servidor
        # El localhost representa "esta computadora" en cualquier red.
        self.host = "0.0.0.0"

        # Definimos un puerto al cual el servidor va a estar escuchando
        self.port = 12345

        # Inicializar socket principal del servidor.
        self.socket_servidor = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)

        # Liberar socket por si alguien mas lo estaba usando
        self.socket_servidor.setsockopt(
            socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # El método bind enlaza el servidor con el puerto y la dirección.
        # Cualquier cosa que llegue al puerto antes puesto va a ser 'escuchado' por
        # el servidor
        self.socket_servidor.bind((self.host, self.port))
        print("Dirección y puerto enlazados..")

        # Luego, con el método listen hacemos que el servidor escuche conexiones
        # entrantes. El entero que se le pasa es el llamado 'backlog', el cual
        # representa el número de conexiones máxima que va a tener en espera de ser aceptadas
        self.socket_servidor.listen(2)
        print("Servidor escuchando en {}:{}...".format(self.host, self.port))

        # Inicializamos un thread para aceptar conexiones entrantes. Es útil
        # usar un thread para que el programa pueda realizar otras cosas
        # por mientras que acepta conexiones
        thread = threading.Thread(
            target=self.accept_connections_thread, daemon=True)
        thread.start()
        print("Servidor aceptando conexiones...")

        # Finalmente, se inicializan un conjunto de estructuras para la lógica del juego
        self.jugadores = {}
        self.sockets = {'jugador_1': None, 'jugador_2': None}
        self.jugada = {'jugador_1': None, 'jugador_2': None}

    def accept_connections_thread(self):
        '''
        Este método es utilizado en el thread para ir aceptando conexiones de
        manera asíncrona al programa principal
        :return:
        '''

        while True:

            # El método accept espera (queda esperando) hasta que algún cliente
            # se conecte y luego retorna una tupla con el socket del cliente
            # recién conectado y la dirección de ésto.
            # Nosotros sólo guardamos el socket.
            client_socket, _ = self.socket_servidor.accept()

            # Luego, como el juego se trata de solo dos jugadores, entonces
            # guardamos solo 2 sockets
            if len(self.jugadores) == 0:
                # Si no había nadie conectado, entonces guardamos la referencia
                # de este socket como si fuese jugador_1
                self.jugadores[client_socket] = 'jugador_1'
                self.sockets["jugador_1"] = client_socket
            elif len(self.jugadores) == 1:
                # Si ya había alguien conectado, entonces lo guardamos como
                # jugador_2
                self.jugadores[client_socket] = 'jugador_2'
                self.sockets["jugador_2"] = client_socket

            print("Servidor conectado a un nuevo cliente...")

            # inicializamos un thread para escuchar a la conexión recién aceptada
            # Por lo que cada cliente conectado va a tener su propio Thread
            # escuchándolo.
            # Pasamos como argumento el socket actual
            listening_client_thread = threading.Thread(
                target=self.listen_client_thread,
                args=(client_socket,),
                daemon=True
            )
            listening_client_thread.start()

            if len(self.jugadores) == 2:
                # Ya aceptó 2 conexiones, por lo que deja de escuchar
                break

    def listen_client_thread(self, client_socket):
        '''
        Este método va a ser usado múltiples veces en threads pero cada vez con
        sockets de clientes distintos.
        :param client_socket: objeto socket correspondiente a algún cliente
        :return:
        '''

        while True:
            # Primero recibimos los 4 bytes del largo
            response_bytes_length = client_socket.recv(4)
            # Los decodificamos
            response_length = int.from_bytes(response_bytes_length,
                                             byteorder="big")

            # Luego, creamos un bytearray vacío para juntar el mensaje
            response = bytearray()

            # Recibimos datos hasta que alcancemos la totalidad de los datos
            # indicados en los primeros 4 bytes recibidos.
            while len(response) < response_length:
                response += client_socket.recv(256)

            # Una vez que tenemos todos los bytes, entonces ahí decodificamos
            response = response.decode()

            # Luego, debemos cargar lo anterior utilizando json
            decoded = json.loads(response)

            # Para evitar hacer muy largo este método, el manejo del mensaje se
            # realizará en otro método
            self.handle_command(decoded, client_socket)

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

        # Aquí se ve qué tipo de mensaje corresponde el que acaba de arribar

        # Si el tipo de mensaje es de eleccion de jugada, entramos
        if received["status"] == "eleccion":

            # Si el jugador correspondiente no tiene jugada asociada, entramos
            # Esto es para evitar que cambie su jugada o haga más de una
            if self.jugada[self.jugadores[client_socket]] is None:

                # Le asignamos su jugada correspondiente
                self.jugada[self.jugadores[client_socket]] = received["data"]

                # Aprovechamos de verificar si ambos jugadores ya jugaron para
                # realizar la lógica del juego
                if None not in self.jugada.values():
                    # Si ambos lanzaron sus dados, jugamos
                    self.play_time()

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
            res_1 = "😂👌💯 Gana 😂👌💯"
            res_2 = "❌ Pierde ❌"
        else:
            res_2 = "😂👌💯 Gana 😂👌💯"
            res_1 = "❌ Pierde ❌"

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

        # Le hacemos json.dumps y luego lo transformamos a bytes
        msg_json = json.dumps(value)
        msg_bytes = msg_json.encode()

        # Luego tomamos el largo de los bytes y creamos 4 bytes de esto
        msg_length = len(msg_bytes).to_bytes(4, byteorder="big")

        # Finalmente, los enviamos al servidor
        socket.send(msg_length + msg_bytes)


if __name__ == "__main__":

    server = Server()

    # Mantenemos al server corriendo
    while True:
        pass
