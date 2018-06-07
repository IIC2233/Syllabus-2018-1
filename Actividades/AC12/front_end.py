import sys
import json
import pickle
import os
import shutil
from back_end import generar_personas, serializar_personas, agregar_estilo, cargar_personas
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel


ventana = uic.loadUiType("gui/ventana.ui")


class Ventana(ventana[0], ventana[1]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setUp()

    def setUp(self):
        self.boton_serializar.clicked.connect(self.serializar)
        self.boton_deserializar.clicked.connect(self.revivir)
        self.boton_estilo.clicked.connect(self.agregar_estilo)
        self.boton_cargar.clicked.connect(self.cargar_personas)
        self.boton_mostrar.clicked.connect(self.mostrar_personas)
        self.personas = None
        self.personas_json = {}
        self.show()

    @property
    def contador(self):
        return "Nº Personas: {}".format(len(self.personas))

    def limpiar_scroll_area(self):
        for i in reversed(range(self.area.layout().count())):
            self.area.layout().itemAt(i).widget().setParent(None)

    def agregar_estilo(self):
        estilo = json.loads(agregar_estilo())
        for i, j in estilo.items():
            self.__dict__[i].setStyleSheet(j)
        self.boton_serializar.setText("")
        self.boton_deserializar.setText("")
        self.label_principal.setText("")
        self.repaint()

    def cargar_personas(self):
        self.personas = cargar_personas()
        self.label_personas.setText(self.contador)
        self.repaint()

    def mostrar_personas(self):
        self.personas_json = {}
        self.limpiar_scroll_area()
        generar_personas(self.personas)
        for path in os.listdir("Personas"):
            path = os.path.join("Personas", path)
            with open(path) as file:
                data = json.load(file)
                text = "Nombre: {}\nApellido: {}\nNumero Alumno: {}"\
                    .format(data["Nombre"],
                            data["Apellido"],
                            data["Numero de Alumno"])
                label = QLabel(text, self)
                self.personas_json[label] = data
                self.area.layout().addWidget(label)
                self.boton_serializar.setEnabled(True)
        self.repaint()

    def serializar(self):
        serializar_personas(self.personas)
        elegidos = [i.split(".")[0] for i in os.listdir("Serializados")]
        elegidos = list(filter(lambda p: p["Numero de Alumno"] in elegidos, self.personas_json.values()))
        for persona in elegidos:
            for label, p in self.personas_json.items():
                if persona == p:
                    label.setStyleSheet("background-color: rgba(252, 0, 6, 203);")
        self.boton_deserializar.setEnabled(True)

    def revivir(self):
        for path in os.listdir("Serializados"):
            path = os.path.join("Serializados", path)
            with open(path, "rb") as file:
                persona = pickle.load(file)
        for i in self.personas_json: i.setStyleSheet("")
        shutil.rmtree('Serializados')



if __name__ == '__main__':

    def hook(type, value, traceback):
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    ventana = Ventana()
    sys.exit(app.exec_())
