__author__ = "DQuezadaO & fgbruna"
__credits__ = ["chapito96", "fringlesinthestreet"]

import sys
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.Qt import QTest
from PyQt5.QtGui import QPixmap, QFont, QIcon
from Ayudantia13_cliente import Client
from Ayudantia13_Eventos import EleccionBotonEvent
from random import randint

# Cargamos la ventana
ventana = uic.loadUiType("ayudantia_13.ui")

class Widget(*ventana):

    '''
    Ventana principal
    '''

    # Señal para avisar al cliente que un botón fue apretado
    trigger_boton = pyqtSignal(EleccionBotonEvent)

    def __init__(self):
        super().__init__()
        # Como usamos Designer, debemos inicializarlo
        self.setupUi(self)

        # Conectamos los botones con sus correspondientes opciones:
        self.dado1.clicked.connect(lambda: self.oprimir_boton(0))
        self.dado2.clicked.connect(lambda: self.oprimir_boton(1))

        # Comienza habilitado
        self.habilitado = True
        self.boton1 = False
        self.boton2 = False
        self.suma = 0

        # Cambiamos la fuente de las letras para que se visualicen mejor
        self.nombre_1.setFont(QFont('SansSerif', 25))
        self.nombre_2.setFont(QFont('SansSerif', 25))
        self.timer.setFont(QFont('SansSerif', 30))
        self.setWindowTitle("🎲 PyQDados 🎲")

        # Inicializamos al cliente y le pasamos a la ventana principal como argumento
        self.client = Client()

        # Comentamos la señal trigger_boton al método del cliente
        self.trigger_boton.connect(self.client.enviar_jugada)
        self.client.trigger_resultados.connect(self.desplegar_resultado)

        self.show()

    def oprimir_boton(self, eleccion):
        '''
        Este método se ejecuta al apretar uno de las tres imágenes.
        Deshabilita el uso del resto de los botones y emite la señal trigger_boton
        :param eleccion: string que puede ser 'papel', 'tijera' y 'piedra'
        :return:
        '''

        # Solo realiza si está habilitado realiza la acción
        if self.habilitado:

            if not eleccion and not self.boton1:
                self.boton1 = True
                numero = randint(1, 6)
                self.dado1.setIcon(QIcon("Assets/{}.png".format(numero)))
                self.suma += numero
            elif eleccion and not self.boton2:
                self.boton2 = True
                numero = randint(1, 6)
                self.dado2.setIcon(QIcon("Assets/{}.png".format(numero)))
                self.suma += numero
            if self.boton1 and self.boton2:
                self.habilitado = False
                event = EleccionBotonEvent(self.suma)
                # Emita la señal hacia el cliente para que envía la jugada al servidor
                self.trigger_boton.emit(event)
                self.suma = 0
                self.boton1, self.boton2 = False, False


    def desplegar_resultado(self, event):
        '''
        Esta función se encarga de mostrar los resultados.
        :param event: instancia de ResultadosEvent. Contiene la información
        :return:
        '''

        # Comienza el conteo
        self.timer.setText("3")
        QTest.qWait(1000)

        self.timer.setText("2")
        QTest.qWait(1000)

        self.timer.setText("1")
        QTest.qWait(1000)

        # Se muestran las opciones elegidas por el usuario y el contrincante
        self.timer.setText("")
        self.eleccion_1.setPixmap(QPixmap("Assets/{}.png".format(event.eleccion_1)))
        self.eleccion_2.setPixmap(QPixmap("Assets/{}.png".format(event.eleccion_2)))

        # Se esperan otros 2 segundos
        QTest.qWait(2000)

        # Sacamos las imágenes de las jugadas
        self.eleccion_1.clear()
        self.eleccion_2.clear()

        # Mostramos el resultado en el centro de la interfaz
        self.timer.setText(event.result)

        # Luego de dos segundos, se borra el mensaje del centro y se vuelve a habilitar
        QTest.qWait(2000)
        self.timer.setText("")
        self.habilitado = True
        self.dado1.setIcon(QIcon("Assets/dice.png"))
        self.dado2.setIcon(QIcon("Assets/dice.png"))

if __name__ == '__main__':

    app = QApplication([])
    form = Widget()
    sys.exit(app.exec_())
