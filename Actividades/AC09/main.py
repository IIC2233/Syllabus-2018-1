"""
-- main.py --

Este módulo cuenta con tres clases:
- Tarea,
- Programador,
- Administrador.
"""

from itertools import count
from random import randint
import threading
import time


TOTAL = 8 * 60 * 60  # segundos de simulación --> ocho horas
VELOCIDAD = 3600     # rapidez según el tiempo de simulación

# Esta simple función te permite simular minutos de trabajo.
reloj = lambda minutos: time.sleep(minutos * 60 / VELOCIDAD)


class Tarea:
    """
    Pequeña clase que modela una tarea.
    """

    id_iter = count(1)

    def __init__(self):
        """
        Inicializa una nueva tarea.
        Le asigna un identificador, un estado de completitud y una duración.
        """

        self.id_ = next(Tarea.id_iter)
        self._hecho = 0
        self.duracion = randint(30, 120)

    def avanzar(self):
        """
        Permite desarrollar una unidad de trabajo de la tarea.
        Retorna un booleano que indica si la tarea está lista.
        """

        self._hecho += 1
        return self._hecho == self.duracion

    def __repr__(self):
        return f'T{self.id_} [{self._hecho}/{self.duracion}]'


class Programador(threading.Thread):
    """
    Pequeña clase que modela un programador.
    """

    pass


class Administrador:
    """
    Pequeña clase que modela un administrador.
    """

    pass


if __name__ == '__main__':
    # Aquí tienes una lista con ocho nombres para los programadores.
    # No hay un bonus por reconocer cuál es la temática entre ellos.

    nombres = [
        'Alex',
        'Matt',
        'Jamie',
        'Nick',
        'Nebil',
        'Belén',
        'Cristian',
        'Jaime',
    ]

    # Aquí deberías escribir unas pocas líneas de código.
    # Hmmm... por ejemplo, crear las instancias en juego.
    # ###################################################



    # ###################################################

    tiempo_inicial = time.time()
    while time.time() - tiempo_inicial < (TOTAL / VELOCIDAD):
        pass
        # Aquí comienza la simulación síncrona.
        # Deberías escribir algo de código acá.
        # (Recuerda borrar el pass, obviamente)
        # #####################################



        # #####################################

    print('Fin de simulación.')
