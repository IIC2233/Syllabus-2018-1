from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QLineEdit, QGridLayout
from back_end import Mario
from Eventos import MoveMarioEvent
import sys

__author__ = "Javier Dreves y Tomás Rivera"

class Menu(QWidget):
    def __init__(self):
        """
        Preparamos la interfaz gráfica del login
        """
        super().__init__()
        self.init_gui()

    def init_gui(self):
        """
        Agregamos los componentes necesarios con algunas conecciones
        """
        self.setWindowTitle("Menu de inicio")
        self.setGeometry(200, 200, 300, 300)

        self.input = QLineEdit('', self)
        self.button1 = QPushButton('Inicio', self)
        self.button2 = QPushButton('Salir', self)
        self.button3 = QPushButton("Ingresar nombre", self)

        self.label = QLabel("Nombre no ingresado", self)
        self.grilla = QGridLayout()  # creamos la grilla

        self.grilla.addWidget(self.input, 0, 0) # le añadimos los componentes a la grilla
        self.grilla.addWidget(self.button3, 0, 1)
        self.grilla.addWidget(self.button1, 1, 0)
        self.grilla.addWidget(self.label, 1,  1)
        self.grilla.addWidget(self.button2, 2, 1)

        self.setLayout(self.grilla) #setiamos la grilla

        self.button2.clicked.connect(self.close) #conectamos el button2 con la funcion self.close
        self.button3.clicked.connect(self.set_name) #conectamos el button3 con la funcion self.set_name

    def set_name(self):
        boton = self.sender() #esto nos retorna el boton al que le hicieron click
        boton.disconnect() #desconectamos el button3 para que no se pueda ingresar nombre de nuevo
        self.label.setText(self.input.text()) # cambiamos el contenido del label
        self.button1.clicked.connect(self.start) #ahora si podemos conectar el button1 a la funcion start

    def start(self):
        self.screen = Screen() #Creamos el widget screen
        self.hide() #Escondemos el widget Menu
        self.screen.show() #Y mostramos el widget screen

    def close(self):
        exit()

class Screen(QWidget):

    trigger_move_mario = pyqtSignal(MoveMarioEvent) #señal para mover mario en el backend
    trigger_jump_mario = pyqtSignal() #señal para hacer saltar el mario en el backend

    def __init__(self, *args, **kwargs):
        """
        Preparamos la interfaz gráfica
        """
        super().__init__(*args, **kwargs)
        self.init_gui()

    def init_gui(self):
        """
        Hacemos todos los ajustes necesarios para conectar la interfaz
        """
        self.setGeometry(200, 100, 800, 600)
        self.setWindowTitle('Mario Bros')

        self.background = QLabel(self)
        self.pixmap = QPixmap("background.png")
        self.background.setPixmap(self.pixmap) #asi setiamos una foto a un label

        self.back_end_mario = Mario(self) #creamos una instancia de mario
        self.trigger_move_mario.connect(self.back_end_mario.move) #conectamos esta señal con la funcion move del frontend
        self.trigger_jump_mario.connect(self.back_end_mario.jump) #conectamos esta señal con la funcion jump del frontend

        self.mario = QLabel('', self)
        self.mario.setGeometry(self.back_end_mario.x,
                               496 - self.back_end_mario.y, 32, 64) # setiamos las dimensiones de mario
        self.mario.setPixmap(QPixmap("sprite/Super Mario.png")) # setiamos la foto inicial de mario
        self.current_pix = 0 #esta variable tendra el sprite que corresponda cuando mario este corriendo

        self.show()

    def keyPressEvent(self, e):
        """
        esta funcion se ejecuta cada vez que se apreta una tecla
        :param e: tecla apretada
        """
        if e.key() == Qt.Key_D: # si la tecla apretada es igual a "D"
            self.current_pix += 1 #cambiamos la imagen a ser mostrada
            if self.current_pix > 3: # solo hay tres imagenes por lo que si es mayor a 3
                self.current_pix = 1 # vuelve a la primera imagen
            self.mario.setPixmap(QPixmap(
                "sprite/Super Mario - Walk{}.png".format(self.current_pix))) #setiamos la imagen correspondiente
            self.trigger_move_mario.emit(MoveMarioEvent("right")) #mandamos señal al backend de que el mario se moverá hacia la derecha

        elif e.key() == Qt.Key_A: # hacemos lo mismo para que al apretar "A" se mueva a la izquierda
            self.current_pix += 1
            if self.current_pix > 3:
                self.current_pix = 1
            self.mario.setPixmap(QPixmap(
                "sprite/Super Mario - Walk{}L.png".format(self.current_pix)))
            self.trigger_move_mario.emit(MoveMarioEvent("left"))

        elif e.key() == Qt.Key_W: #si se apreta la tecla "W"
            if self.back_end_mario.facing == "right": #si mario mira hacia la derecha
                self.mario.setPixmap(QPixmap("sprite/Super Mario - Jump.png")) #cambiamos su imagen por mario saltando a la derecha
            else: #si no
                self.mario.setPixmap(QPixmap("sprite/Super Mario - JumpL.png")) #cambiamos su imagen por mario saltando a la izquierda
            self.trigger_jump_mario.emit() #emitimos la señal al backend para que mario salte
            if self.back_end_mario.facing == "right": #cuando termine de saltar, cambiamos su imagen por mario normal (der o izq)
                self.mario.setPixmap(QPixmap("sprite/Super Mario.png"))
            else:
                self.mario.setPixmap(QPixmap("sprite/Super MarioL.png"))

        elif e.key() == Qt.Key_S: #si se apreta la tecla "S", se cambia la imagen de mario por mario agachado (der o izq)
            if self.back_end_mario.facing == "right":
                self.mario.setPixmap(QPixmap("sprite/Super Mario - Duck.png"))
            else:
                self.mario.setPixmap(QPixmap("sprite/Super Mario - DuckL.png"))
            self.mario.move(self.back_end_mario.x, 506 - self.back_end_mario.y) #movemos el label con la imagen de mario

    def keyReleaseEvent(self, e):
        """
        Funcion que se ejecuta cada vez que se suelta una tecla
        :param e: tecla soltada
        """
        if e.key() == Qt.Key_D: # Si se suelta la tecla "D"
            self.mario.setPixmap(QPixmap("sprite/Super Mario.png")) #Su imagen deja de correr

        elif e.key() == Qt.Key_A: # Si se suelta la tecla "A"
            self.mario.setPixmap(QPixmap("sprite/Super MarioL.png")) #Su imagen deja de correr

        elif e.key() == Qt.Key_S: # Si se suelta la tecla "S"
            if self.back_end_mario.facing == "right": #dependiendo de donde mira
                self.mario.setPixmap(QPixmap("sprite/Super Mario.png")) #Su imagen deja correr
            else:
                self.mario.setPixmap(QPixmap("sprite/Super MarioL.png"))
            self.mario.move(self.back_end_mario.x, 496 - self.back_end_mario.y)

    def move_mario(self, event):
        """
        Funcion que actualiza el label de mario
        :param event: Evento que contiene las coordenadas de mario (x, y)
        """
        self.mario.move(event.x, 496 - event.y)

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)


    sys.__excepthook__ = hook
    app = QApplication([])
    inicio = Menu()
    inicio.show()
    app.exec_()
