from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.Qt import QTest
from Eventos import MoveEvent

class Mario(QObject):

    move_mario = pyqtSignal(MoveEvent) #Señal para mover la imagen de mario en el frontend

    def __init__(self, parent):
        super().__init__()
        self._x = 100 #posicion x de mario
        self.y = 0 #posicion y de mario
        self.facing = "right" #orientacion de mario
        self.jumping = False #True si mario está saltando
        self.move_mario.connect(parent.move_mario) #Conectamos la señal a la funcion move_mario del frontend

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        """
        Este setter verifica que mario no se salga de los margenes
        :param value: valor al que se va a setear
        """
        if value < 0:
            self._x = 0
        elif value > 770:
            self._x = 770
        else:
            self._x = value

    def set_y(self, y):
        """
        Setea el valor del atributo self.y
        :param y: Valor resultante
        """
        self.y = y


    def refresh_pos(self):
        """
        Emite la señal a la interdaz gráfica
        para que se actualize la imagen de mario
        """
        self.move_mario.emit(MoveEvent(self.x, self.y))

    def move(self, event):
        """
        Cambia la posición de Mario dependiendo de su orientacio
        y llama a refresh_pos para actualizar su posicion en el frontend
        :param event: Evento con el lado del movimiento
        """
        if event.side == "right":
            self.x += 5
            self.facing = "right"
        elif event.side == "left":
            self.x -= 5
            self.facing = "left"
        self.refresh_pos()

    def jump(self):
        """
        Funcion que realiza el salto de mario
        """
        initial_y = self.y #guardamos el y inicial
        if not self.jumping: #ejecutamos el salto solo si no está saltando
            self.jumping = True #setiamos el salto como True
            for i in range(1, 51):
                self.set_y(initial_y + 4*i) #cambiamos la posicion y de mario 4 pixeles hacia arriba por iteracion
                self.refresh_pos() #actualiza la posicion del mario en el frontend
                QTest.qWait(10) #espera 1/100 de segundo
            for i in range(1, 51):
                self.set_y(initial_y + 50*4 - 4*i) # cambiamos la posicion y de mario 4 pixeles hacia abajo por iteracion
                self.refresh_pos() ##actualiza la posicion del mario en el frontend
                QTest.qWait(10) #espera 1/100 de segundo
            self.jumping = False #Mario deja de saltar
