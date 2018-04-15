from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, \
    QGroupBox, QLineEdit, QScrollArea, QGridLayout, QFrame

newfont = QFont("Copperplate Gothic Light", 8,
                QFont.Black)

smallfont = QFont("Copperplate Gothic Light", 8,
                QFont.Black)

mediumfont = QFont("Copperplate Gothic Light", 10,
                QFont.Black)

boton_yeah = """
QPushButton{
    background-color: rgb(255,255,255,70%);
    border-width: 1px;
    border-radius: 20px;
}
QPushButton::pressed {
    background-color: rgb(0, 0, 0,75%);

}"""
mini_boton_yeah = """
QPushButton{
    background-color: rgb(255,255,255,70%);
    border-width: 1px;
    border-radius: 10px;
}
QPushButton::pressed {
    background-color: rgb(0, 0, 0,75%);

}"""
frame_yeah = """
QFrame{
background-color: rgb(255,255,255,20%);
border-width : 5px;
border-radius: 10px
}"""

label_yeah = """
QLabel{
background-color:rgb(255,255,255, 100%);
    border-width: 1px;
    border-radius: 15px
    }"""


class Scroll(QScrollArea):
    def __init__(self, jugadores, parent):
        super().__init__(parent)
        self.contador = 0
        self.content = QWidget(parent)
        self.layout = QGridLayout(self.content)
        self.setStyleSheet('background-color:rgba(0,50,0,20%)')
        self.jugadores = []
        col = 0
        for jugador in jugadores:
            col += 1
            self.layout.addWidget(jugador.layout, 0, col)
            self.jugadores.append(jugador)
        self.setWidget(self.content)
        self.setMinimumWidth(1366)
        self.setGeometry(0, 0, 1250, 130)

    def intercambio(self, j1, j2 = None):
        x = next(x for x in self.jugadores if x.id == j1.id)
        if j2:
            self.jugadores[self.jugadores.index(x)] = j2
        else:
            self.jugadores.pop(self.jugadores.index(x))
        lista = []
        self.content = QWidget(self.parent())
        self.layout = QGridLayout(self.content)
        col = 0
        for jugador in self.jugadores:
            col += 1
            jugador.create_layout()
            self.layout.addWidget(jugador.layout,0,col)
            lista.append(jugador)
        self.jugadores = lista
        self.setWidget(self.content)

    def mostrar_busqueda(self, lista):
        self.content = QWidget(self.parent())
        self.layout = QGridLayout(self.content)
        col = 0
        for jugador in lista:
            col += 1
            jugador.create_layout()
            self.layout.addWidget(jugador.layout,0,col)
        self.setWidget(self.content)

class Layout(QFrame):
    def __init__(self, parent, jugador, scaled):
        super().__init__(parent)
        self.jugador = jugador
        self.setGeometry(0,0,100*scaled, 100*scaled)
        self.setFixedSize(100 * scaled, 100 * scaled)

    def mousePressEvent(self, event):
        self.jugador.mousePressEvent()


class Jugador:

    def __init__(self, parent, id, nombre, nombre_completo, club,
                 liga, nacionalidad, overall, scaled = 1):

        self.parent = parent
        self.id = id
        self.nombre = nombre
        self.nombre_completo = nombre_completo
        self.club = club
        self.liga = liga
        self.nacionalidad = nacionalidad
        self.overall = overall
        self.scaled = scaled
        self.layout = Layout(parent, self, scaled)
        self.layout.setStyleSheet(frame_yeah)
        self.label = QLabel(self.layout)
        self.label.setPixmap(QPixmap('assets/photo/' + id).scaled(100 * scaled, 100* scaled))
        self.en_cancha = False
        self.x = 0
        self.y = 0

    def move(self, x, y):
        self.layout.move(x,y)
        self.x = x
        self.y = y

    def show(self):
        self.layout.show()

    def hide(self):
        self.layout.hide()

    def mousePressEvent(self):
        if self.parent.listo:
            if not self.en_cancha and self.parent.booleanos['k']:
                self.parent.intercambio(self)
            elif self.parent.booleanos['k']:
                self.parent.intercambio(self, True)
            else:
                self.parent.seleccion(self)
        elif not self.en_cancha:
            self.parent.agregar_jugador(self)

    def create_layout(self):
        self.layout = Layout(self.parent, self, self.scaled)
        self.layout.setStyleSheet(frame_yeah)
        self.label = QLabel(self.layout)
        self.label.setPixmap(QPixmap('assets/photo/' + self.id).scaled(100 * self.scaled, 100* self.scaled))

class CuadroInfo:

    def __init__(self, parent, jugador):
        self.parent = parent
        self.layout = QGroupBox(self.parent)
        self.layout.setGeometry(0,0, 240, 240)
        self.layout.setStyleSheet('background-color:rgba(0,0,40,80%)')
        self.imagen = QLabel(self.layout)
        self.imagen.setPixmap(QPixmap('assets/photo/' + jugador.id).scaled(100, 100))
        self.imagen.move(0,0)

        self.label_nombre = QLabel(self.layout)
        self.label_nombre.setText('Nombre: '+ jugador.nombre)
        self.label_nombre.setGeometry(10, 103, 220, 14)
        self.label_nombre.setFont(newfont)
        self.label_nombre.setStyleSheet('background-color: green')

        self.label_club = QLabel(self.layout)
        self.label_club.setText('Club: ' + jugador.club)
        self.label_club.setGeometry(10, 125, 220, 14)
        self.label_club.setFont(newfont)
        self.label_club.setStyleSheet('background-color: green')

        self.label_nacionalidad = QLabel(self.layout)
        self.label_nacionalidad.setText('Nacionalidad: ' + jugador.nacionalidad)
        self.label_nacionalidad.setGeometry(10, 147, 220, 14)
        self.label_nacionalidad.setFont(newfont)
        self.label_nacionalidad.setStyleSheet('background-color: green')

        self.label_liga = QLabel(self.layout)
        self.label_liga.setText('Liga: ' + jugador.liga)
        self.label_liga.setGeometry(10, 169, 220, 14)
        self.label_liga.setFont(newfont)
        self.label_liga.setStyleSheet('background-color: green')

        self.label_overall = QLabel(self.layout)
        self.label_overall.setText('Overall: ' + jugador.overall)
        self.label_overall.setGeometry(10, 191, 220, 14)
        self.label_overall.setFont(newfont)
        self.label_overall.setStyleSheet('background-color: green')

        self.boton_cambio = QPushButton('Cambiar', self.layout)
        self.boton_cambio.clicked.connect(lambda : self.parent.cambio(jugador))
        self.boton_cambio.setStyleSheet('background-color: gray')
        self.boton_cambio.setGeometry(105, 30, 120, 45)

        self.layout.show()

    def hide(self):
        self.layout.hide()

    def move(self, x, y):
        self.layout.move(x, y)


class MyLineEdit(QLineEdit):

    def __init__(self, text, parent):
        super().__init__(text, parent)
        self.texto = text

    def mousePressEvent(self, event):
        if self.text() == self.texto:
            self.setText('')
            self.setFont(self.parent().smallfont)

    def reset(self):
        self.setFont(self.parent().italicfont)
        self.setText(self.texto)
        self.clearFocus()
