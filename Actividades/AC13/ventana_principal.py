#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal, Qt, QSize
from PyQt5.QtGui import QPixmap, QPalette, QImage, QBrush
from time import sleep
from random import randint
import sys

class EventoMoverImagen:

    def __init__(self, label, imagen, x, y):
        self.label = label
        self.imagen = imagen
        self.x = x
        self.y = y


class MoveThread:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Personaje(QThread):
    desencadenar = pyqtSignal(EventoMoverImagen)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    # objeto clase EventoMoverImagen, podria ser tambien int o str en caso
    # de que busquemos enviar este tipo de objetos en la senal.

    def __init__(self, padre, x, y):
        """
        Un Personaje es un QThread que moverá una imagen de una pelota
        en una ventana. El __init__ recibe los parametros:
            padre: ventana
            x e y: posicion inicial en la ventana
        """
        super().__init__()
        # Guardamos el path de la imagen que tendrá el Label
        self.imagen = "assets/abajo/1.png"
        # Creamos el Label y definimos su tamaño
        self.label = QLabel(padre)
        self.label.setGeometry(x, y, 50, 50)
        self.label.setPixmap(QPixmap(self.imagen))
        self.label.setScaledContents(True)
        self.label.show()
        self.label.setVisible(True)
        # Seteamos la posición inicial y la guardamos para usarla como una property
        self.__posicion = (0, 0)
        self.__numero_imagen = 1
        self.orientacion_imagen = "abajo"
        self.posicion = (x, y)
        #Guardamos los limites de la ventana para que no pueda salirse de ella
        self.start()

    @property
    def numero_imagen(self):
        return self.__numero_imagen

    @numero_imagen.setter
    def numero_imagen(self, value):
        if value > 3:
            self.__numero_imagen = 1
        else:
            self.__numero_imagen = value

    def actualizar_posicion(self, nuevo_pos):
        self.posicion = nuevo_pos

    @property
    def posicion(self):
        return self.__posicion

    @posicion.setter
    def posicion(self, value):
        orientacion = self.obtener_orientacion(self.posicion, value)
        if orientacion != self.orientacion_imagen:
            self.numero_imagen = 0
        self.orientacion_imagen = orientacion
        self.numero_imagen += 1
        imagen = "assets/{}/{}.png".format(self.orientacion_imagen, self.numero_imagen)
        self.__posicion = value
        # El desencadenar emite su senal a la ventana cuando cambiamos la posición
        self.desencadenar.emit(EventoMoverImagen(
            self.label, imagen, self.posicion[0], self.posicion[1]
        ))

    def obtener_orientacion(self, pos_1, pos_2):
        if pos_2[1] - pos_1[1] > 0:
            return "abajo"
        elif pos_2[1] - pos_1[1] < 0:
            return "arriba"
        elif pos_2[0] - pos_1[0] > 0:
            return "derecha"
        elif pos_2[0] - pos_1[0] < 0:
            return "izquierda"
        else:
            return self.orientacion_imagen


    def run(self):
        while True:
            sleep(0.1)


class MiVentana(QMainWindow):

    senal_nuevo_personaje = pyqtSignal(tuple)
    senal_mi_personaje = pyqtSignal(tuple)
    senal_eliminar_personaje = pyqtSignal()
    senal_cerrado = pyqtSignal()

    def __init__(self, funcion_mover, funcion_cerrado):
        super().__init__()
        self.setWindowTitle("AC13")
        self.setGeometry(100, 100, 1200, 800)
        img, palete = QImage("assets/fondo.png"), QPalette()
        palete.setBrush(10, QBrush(img.scaled(QSize(1200, 800))))
        self.setAutoFillBackground(False)
        self.setPalette(palete)
        self.show()
        self.senal_mi_personaje.connect(self.crear_mi_personaje)
        self.senal_eliminar_personaje.connect(self.eliminar_thread_personaje)
        self.funcion_mover = funcion_mover
        self.senal_cerrado.connect(funcion_cerrado)


    def crear_mi_personaje(self, tupla):
        x_inicial, y_inicial = tupla
        self.mi_personaje = Personaje(padre=self, x=x_inicial, y=y_inicial)
        self.mi_personaje.desencadenar.connect(self.actualizar_imagen)

    def agregar_mi_personaje(self, x_inicial, y_inicial):
        #Agrega el personaje en x, y
        self.senal_mi_personaje.emit((x_inicial, y_inicial))


    def keyPressEvent(self, evento):
        # Este va a llamar a funcion_mover que se entrega cuando se instancia la ventana
        step = 3
        x, y = self.mi_personaje.posicion
        if evento.key() == Qt.Key_Left:
            self.funcion_mover(max(x - step, 0), y)
        elif evento.key() == Qt.Key_Right:
            self.funcion_mover(min(x + step, 1200), y)
        elif evento.key() == Qt.Key_Up:
            self.funcion_mover(x, max(y - step, 0))
        elif evento.key() == Qt.Key_Down:
            self.funcion_mover(x, min(y + step, 800))

    def actualizar_posicion_personaje(self, x, y):
        #Con este actualizamos la posicion
        self.mi_personaje.posicion = (x, y)

    @staticmethod
    def actualizar_imagen(miEventoImagen):
        # Recibo el objeto con la información necesaria para mover a la comida
        label = miEventoImagen.label
        pixmap = QPixmap(miEventoImagen.imagen)
        label.setPixmap(pixmap)
        label.move(miEventoImagen.x, miEventoImagen.y)

    def eliminar_personaje(self):
        # Con este se elimina el personaje
        self.senal_eliminar_personaje.emit()

    def eliminar_thread_personaje(self):
        self.mi_personaje.quit()
        self.mi_personaje.label.deleteLater()

    def closeEvent(self, QCloseEvent):
        self.senal_cerrado.emit()
        super().closeEvent(QCloseEvent)



if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)
        print("___\n")
    sys.__excepthook__ = hook
    def mover(x, y):
        print(x, y)
    def cerrar():
        print("cerrando")
    app = QApplication([])
    ex = MiVentana(mover, cerrar)
    ex.agregar_mi_personaje(2, 15)
    app.exec_()
