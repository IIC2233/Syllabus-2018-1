
import socket
import threading


class Servidor:

    def __init__(self):
        # Creamos un socket para una conexión TCP con IPv4
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "localhost"
        port = 10001

        # El metodo bind "enlaza" el socket a un puerto dado, en este caso el puerto 80
        self.socket.bind((host, port))

        # Con el método listen() pedimos al sistema operativo que empiece a escuchar por
        # potenciales conexiones al socket. El argumento corresponde al número máximo de
        # conexiones pendientes permitidas.
        self.socket.listen(5)

        thread = threading.Thread(target=self.accept_clients, daemon=True)

        thread.start()

        self.conexiones = []


    def listen_clients(self, socket):
        s = ""
        while s != "fin":
            data = socket.recv(1024)
            s = data.decode('ascii')
            print(s)
        print("Desconectado")
        socket.close()



    def accept_clients(self):
        cont = 0
        while True:
            # Establecemos la conexión
            socket_cliente, address = self.socket.accept()
            print("Obtuvimos una conexión desde %s" % str(address))
            socket_cliente.send(
                "{}. Hola nuevo amigo!\n".format(cont).encode("ascii"))

            thread = threading.Thread(target = self.listen_clients, args = (socket_cliente, ), daemon=True)

            thread.start()
            cont += 1
            self.conexiones.append(socket_cliente)

    def send_message(self, msg):

        for socket in self.conexiones:
            socket.send("{}".format(msg).encode("ascii"))


s = Servidor()
while True:
    msg = input()
    s.send_message(msg)