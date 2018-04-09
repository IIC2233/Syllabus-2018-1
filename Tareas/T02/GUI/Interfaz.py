from PyQt5.QtGui import QImage, QBrush, QPalette, QFont,QStandardItem,\
    QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget,QPushButton, QLabel, QListView
from clases import Scroll, Jugador, CuadroInfo, boton_yeah, MyLineEdit, \
    label_yeah, mini_boton_yeah
from random import sample


class Window(QWidget):
    def __init__(self, parent, jugadores, equipos):
        super().__init__()
        self.parent = parent
        self.__setUp(jugadores, equipos)

    def __setUp(self, jugadores, equipos):
        self.setGeometry(0, 30, 1366, 697)
        oImage = QImage("Assets/Fondo").scaled(1366,
                                               697)  # Ponemos el Background
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))
        self.setPalette(palette)

        self.newfont = QFont("Copperplate Gothic Light", 12,
                             QFont.Black)

        self.italicfont = QFont("Copperplate Gothic Light", 8)
        self.italicfont.setItalic(True)

        self.smallfont = QFont("Copperplate Gothic Light", 8)

        self.boton_equipo = QPushButton('Mi equipo', self)
        self.boton_equipo.setFont(self.newfont)
        self.boton_equipo.clicked.connect(self.ver_equipo)
        self.boton_equipo.setStyleSheet(boton_yeah)
        self.boton_equipo.setGeometry(613, 225, 140, 45)

        self.boton_campeonatos = QPushButton('Campeonatos', self)
        self.boton_campeonatos.setFont(self.newfont)
        self.boton_campeonatos.clicked.connect(self.campeonatos)
        self.boton_campeonatos.setStyleSheet(boton_yeah)
        self.boton_campeonatos.setGeometry(613, 300, 140, 45)

        self.show()

        self.boton_atras = QPushButton('Atrás', self)
        self.boton_atras.setFont(self.newfont)
        self.boton_atras.clicked.connect(self.atras)
        self.boton_atras.setStyleSheet(boton_yeah)
        self.boton_atras.setGeometry(1275, 1, 90, 40)

        self.__ptje = 60
        self.cuadro_info = QLabel(self)

        self.booleanos = {'e': False, 'j': False,
                          'c': False, 'k': False}

        self.equipos = equipos

        self.lista_jugadores = []
        for i in jugadores:
            self.lista_jugadores.append(Jugador(self, *i, scaled=0.8))

        self.__jugadores = sample(self.lista_jugadores, 11)
        self.__jugadores_afuera = [
            Jugador(self, x.id, x.nombre, x.nombre_completo, x.club, x.liga,
                    x.nacionalidad, x.overall) for x in self.lista_jugadores if
            x not in self.__jugadores]

    def ver_equipo(self):
        oImage = QImage("Assets/cancha_inferior").scaled(1366,
                                                         697)  # Ponemos el Background
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))
        self.setPalette(palette)
        self.booleanos['e'] = True
        self.boton_atras.show()
        self.boton_campeonatos.hide()
        self.boton_equipo.hide()

        self.buscador_jugador = MyLineEdit('buscar jugador', self)
        self.buscador_jugador.setFont(self.italicfont)
        self.buscador_jugador.setGeometry(10, 535, 120, 25)
        self.buscador_jugador.show()

        self.boton_buscar = QPushButton('Buscar', self)
        self.boton_buscar.setFont(self.smallfont)
        self.boton_buscar.setStyleSheet(boton_yeah)
        self.boton_buscar.setGeometry(135, 525, 75, 40)
        self.boton_buscar.clicked.connect(self.buscar)
        self.boton_buscar.show()

        self.label_puntaje = QLabel(self)
        self.label_puntaje.setText(' Esperanza: ' + str(self.__ptje))
        self.label_puntaje.setFont(self.newfont)
        self.label_puntaje.setStyleSheet(label_yeah)
        self.label_puntaje.setGeometry(1200, 520, 160, 40)
        self.label_puntaje.show()

        for i in self.__jugadores_afuera:
            i.create_layout()

        self.scroll_jugadores = Scroll(self.__jugadores_afuera, self)
        self.scroll_jugadores.move(0, 570)
        self.scroll_jugadores.show()

        self.reajustar_formacion()
        for i in self.__jugadores:
            i.en_cancha = True
            i.show()

    def buscar(self):
        lista = []
        for i in self.__jugadores_afuera:
            if self.buscador_jugador.text() in i.nombre_completo:
                lista.append(i)
        if len(lista) > 0:
            self.scroll_jugadores.mostrar_busqueda(lista)

    def seleccion(self, jugador):
        self.cuadro_info.hide()
        if jugador.en_cancha:
            self.cuadro_info = CuadroInfo(self, jugador)
            self.cuadro_info.move(jugador.x, jugador.y)

    def reajustar_formacion(self):
        lista = list(self.__jugadores)
        self.cuadro_info.hide()
        lista[0].move(646, 450)
        lista.pop(0)
        for i in range(4):
            lista[0].move(205 + 300 * i, 350)
            lista.pop(0)
        for i in range(4):
            lista[0].move(195 + 310 * i, 210)
            lista.pop(0)
        for i in range(2):
            lista[0].move(520 + 220 * i, 70)
            lista.pop(0)

    def campeonatos(self):
        oImage = QImage("Assets/torneo").scaled(1366,
                                                697)  # Ponemos el Background
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))
        self.setPalette(palette)
        self.booleanos['c'] = True
        self.boton_atras.show()
        self.boton_campeonatos.hide()
        self.boton_equipo.hide()

        self.label_equipos = QLabel('  Equipos', self)
        self.label_equipos.setGeometry(150, 50, 100, 30)
        self.label_equipos.setFont(self.newfont)
        self.label_equipos.setStyleSheet(label_yeah)
        self.label_equipos.show()

        self.label_resultados = QLabel(' Resultados', self)
        self.label_resultados.setGeometry(538, 50, 124, 30)
        self.label_resultados.setFont(self.newfont)
        self.label_resultados.setStyleSheet(label_yeah)
        self.label_resultados.show()

        self.label_respuestas = QLabel(' Respuestas', self)
        self.label_respuestas.setGeometry(988, 50, 124, 30)
        self.label_respuestas.setFont(self.newfont)
        self.label_respuestas.setStyleSheet(label_yeah)
        self.label_respuestas.show()

        self.boton_simular = QPushButton('Jugar', self)
        self.boton_simular.setStyleSheet(boton_yeah)
        self.boton_simular.setGeometry(350, 150, 100, 45)
        self.boton_simular.clicked.connect(self.simular)
        self.boton_simular.setFont(self.newfont)
        self.boton_simular.show()

        self.boton_random = QPushButton('Al azar', self)
        self.boton_random.setStyleSheet(boton_yeah)
        self.boton_random.setGeometry(350, 250, 100, 45)
        self.boton_random.clicked.connect(lambda: self.simular(True))
        self.boton_random.setFont(self.newfont)
        self.boton_random.show()

        self.consulta_usuario = QPushButton('Datos usuario', self)
        self.consulta_usuario.setEnabled(False)
        self.consulta_usuario.setStyleSheet(mini_boton_yeah)
        self.consulta_usuario.setGeometry(760, 130, 100, 25)
        self.consulta_usuario.setFont(self.smallfont)
        self.consulta_usuario.clicked.connect(lambda: self.consulta(0))
        self.consulta_usuario.show()

        self.consulta_ganadores = QPushButton('Ganadores', self)
        self.consulta_ganadores.setEnabled(False)
        self.consulta_ganadores.setStyleSheet(mini_boton_yeah)
        self.consulta_ganadores.setGeometry(760, 170, 100, 25)
        self.consulta_ganadores.clicked.connect(lambda: self.consulta(2))
        self.consulta_ganadores.setFont(self.smallfont)
        self.consulta_ganadores.show()

        self.edit_equipo = MyLineEdit('Ingrese equipo', self)
        self.edit_equipo.setGeometry(715, 210, 100, 25)
        self.edit_equipo.setFont(self.italicfont)
        self.edit_equipo.show()

        self.consulta_equipo = QPushButton('Consultar', self)
        self.consulta_equipo.setEnabled(False)
        self.consulta_equipo.setStyleSheet(mini_boton_yeah)
        self.consulta_equipo.setGeometry(830, 210, 100, 25)
        self.consulta_equipo.setFont(self.smallfont)
        self.consulta_equipo.clicked.connect(lambda: self.consulta(1))
        self.consulta_equipo.show()

        self.edit_fase = MyLineEdit('Ingrese fase', self)
        self.edit_fase.setGeometry(715, 250, 100, 25)
        self.edit_fase.setFont(self.italicfont)
        self.edit_fase.show()

        self.consulta_fase = QPushButton('Consultar', self)
        self.consulta_fase.setEnabled(False)
        self.consulta_fase.setStyleSheet(mini_boton_yeah)
        self.consulta_fase.setGeometry(830, 250, 100, 25)
        self.consulta_fase.setFont(self.smallfont)
        self.consulta_fase.clicked.connect(lambda: self.consulta(4))
        self.consulta_fase.show()

        self.edit_partido = MyLineEdit('id partido', self)
        self.edit_partido.setGeometry(715, 290, 100, 25)
        self.edit_partido.setFont(self.italicfont)
        self.edit_partido.show()

        self.consulta_partido = QPushButton('Consultar', self)
        self.consulta_partido.setEnabled(False)
        self.consulta_partido.setStyleSheet(mini_boton_yeah)
        self.consulta_partido.setGeometry(830, 290, 100, 25)
        self.consulta_partido.setFont(self.smallfont)
        self.consulta_partido.clicked.connect(lambda: self.consulta(3))
        self.consulta_partido.show()

        self.resultados = QListView(self)
        self.resultados.setGeometry(500, 100, 200, 450)
        self.items_resultado = []
        self.model_resultados = QStandardItemModel(self.resultados)
        self.resultados.show()

        self.respuestas = QListView(self)
        self.respuestas.setGeometry(950, 100, 200, 450)
        self.items_respuestas = []
        self.model_respuestas = QStandardItemModel(self.respuestas)
        self.respuestas.show()

        self.view = QListView(self)
        self.view.setGeometry(100, 100, 200, 450)

        model = QStandardItemModel(self.view)

        item = QStandardItem('Tu equipo, ' + str(self.__ptje))
        item.setCheckable(True)
        item.setEditable(False)
        model.appendRow(item)

        self.items = [item]

        for i in self.equipos:
            item = QStandardItem(i[0] + ', ' + str(i[1]))
            item.setCheckable(True)
            item.setEditable(False)
            model.appendRow(item)
            self.items.append(item)

        self.view.setModel(model)

        self.view.show()

        self.edits = [self.edit_equipo, self.edit_partido, self.edit_fase
                      ]

        self.botones = [self.consulta_partido,
                        self.consulta_fase, self.consulta_usuario,
                        self.consulta_equipo, self.consulta_ganadores]

    def consulta(self, i):
        consultas = [self.parent.consulta_usuario,
                     lambda: self.parent.consulta_equipo(
                         self.edit_equipo.text()),
                     self.parent.consulta_ganadores,
                     lambda: self.parent.consulta_partido(
                         self.edit_partido.text()),
                     lambda: self.parent.consulta_fase(self.edit_fase.text())]
        consultas[i]()

    def simular(self, random=False):
        if not random:
            equipos = []

            for i in self.items:
                if i.checkState() == 2:
                    equipos.append(i.text().split(','))
        else:
            equipos = [x.text().split(',') for x in sample(self.items, 16)]
        if len(equipos) == 16:
            self.parent.simular_campeonato(equipos)
            for i in self.botones:
                i.setEnabled(True)

    def atras(self):
        oImage = QImage("Assets/fondo").scaled(1366,
                                               697)
        palette = QPalette()
        palette.setBrush(10, QBrush(oImage))
        self.setPalette(palette)
        self.boton_equipo.show()
        self.boton_campeonatos.show()
        self.boton_atras.hide()

        if self.booleanos['e']:
            self.label_puntaje.hide()
            self.scroll_jugadores.hide()
            for i in self.__jugadores:
                i.hide()
            self.buscador_jugador.hide()
            self.boton_buscar.hide()
        elif self.booleanos['c']:
            self.view.hide()
            self.boton_simular.hide()
            for i in self.edits:
                i.hide()
            for i in self.botones:
                i.hide()
            self.resultados.hide()
            self.respuestas.hide()
            self.boton_random.hide()
            self.label_respuestas.hide()
            self.label_resultados.hide()
            self.label_equipos.hide()
        for x in self.booleanos:
            self.booleanos[x] = False

    def cambio(self, x):
        self.booleanos['k'] = True
        self.jugador_cambiando = Jugador(self, x.id, x.nombre,
                                         x.nombre_completo, x.club, x.liga,
                                         x.nacionalidad, x.overall)
        self.jugador_seleccionado = x
        self.cuadro_info.hide()

    def intercambio(self, j2, cancha=False):
        i = self.__jugadores.index(self.jugador_seleccionado)
        self.booleanos['k'] = False
        if not cancha:
            self.scroll_jugadores.intercambio(j2, self.jugador_cambiando)
            self.__jugadores[i] = next(
                x for x in self.lista_jugadores if x.nombre == j2.nombre)
            self.reajustar_formacion()
            self.__jugadores[i].show()
            self.__jugadores[i].en_cancha = True
            self.jugador_seleccionado.hide()
            self.jugador_seleccionado.en_cancha = False
            j1 = self.jugador_seleccionado
            j3 = next(x for x in self.__jugadores_afuera if x.id == j2.id)
            self.__jugadores_afuera[
                self.__jugadores_afuera.index(j3)] = Jugador(self, j1.id,
                                                             j1.nombre,
                                                             j1.nombre_completo,
                                                             j1.club, j1.liga,
                                                             j1.nacionalidad,
                                                             j1.overall)
        else:
            j = self.__jugadores.index(j2)
            self.__jugadores[i] = j2
            self.__jugadores[j] = self.jugador_seleccionado
            self.reajustar_formacion()
        self.parent.cambio_jugador(self.jugador_seleccionado.nombre_completo,
                                   j2.nombre_completo, cancha)

    def mousePressEvent(self, event):
        self.cuadro_info.hide()
        self.booleanos['k'] = False
        if self.booleanos['e']:
            self.buscador_jugador.reset()
        if self.booleanos['c']:
            for i in self.edits:
                i.reset()

    def keyPressEvent(self, key):
        if self.booleanos['e'] and key.key() == Qt.Key_Return:
            self.boton_buscar.click()

    @property
    def puntaje(self):
        return self.__ptje

    @puntaje.setter
    def puntaje(self, value):
        self.__ptje = value
        self.label_puntaje.setText(' Esperanza :' + str(value))

    ### funciones para ser utilizadas por alumnos

    def cambiar_esperanza(self,
                        valor):  # decidí hacerlo una función, ya que es más fácil darles una función que explicar que lo deben usar como propiedad.
        self.puntaje = valor

    def agregar_resultado(self, resultado):
        item = QStandardItem(resultado)
        item.setEditable(False)
        self.model_resultados.appendRow(item)
        self.items_resultado.append(item)
        self.resultados.setModel(self.model_resultados)

    def agregar_respuesta(self, respuesta):
        item = QStandardItem(respuesta)
        item.setEditable(False)
        self.model_respuestas.appendRow(item)
        self.items_respuestas.append(item)
        self.respuestas.setModel(self.model_respuestas)

    def resetear_resultados(self):
        self.resultados.hide()
        self.resultados = QListView(self)
        self.resultados.setGeometry(500, 100, 200, 450)
        self.items_resultado = []
        self.model_resultados = QStandardItemModel(self.resultados)
        self.resultados.show()
        for i in self.botones:
            i.setEnabled(False)

    def resetear_respuestas(self):
        self.respuestas.hide()
        self.respuestas = QListView(self)
        self.respuestas.setGeometry(950, 100, 200, 450)
        self.items_respuestas = []
        self.model_respuestas = QStandardItemModel(self.respuestas)
        self.respuestas.show()

