from gui.Gui import MyWindow
from PyQt5 import QtWidgets
import sys


class T03Window(MyWindow):
    def __init__(self):
        super().__init__()

    def process_query(self, queries):
        # Agrega en pantalla la solucion.
        print(queries)
        text = "Probando funcion\nConsulta 01\n"
        self.add_answer(text)

    def save_file(self, queries):
        # Crea un archivo con la solucion.
        print(queries)

if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(value)
        print(traceback)


    sys.__excepthook__ = hook

    app = QtWidgets.QApplication(sys.argv)
    window = T03Window()
    sys.exit(app.exec_())
