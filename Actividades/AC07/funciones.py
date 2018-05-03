from random import uniform
from time import sleep
from collections import namedtuple

Pieza = namedtuple('Pieza', 'nombre estado')


def revisar_estado(trabajador, auto):
    """
    Método correcto para reemplazar en vez de revizar_ztado(auto)
    """

    total = sum([pieza.estado for pieza in auto.piezas])
    estado = round(total / len(auto.piezas), 1)

    print("El auto está reparado en un {} %".format(estado))

    return estado


def reparar(trabajador, auto):
    """
    Utilizado para reparar el auto
    """

    print("Reparando las piezas...esto puede tomar un segundo...(literal)")
    sleep(1)
    auto.piezas = [pieza._replace(estado=100) for pieza in auto.piezas]


def crear_piezas():
    """
    Si no se utiliza, qué piezas vamos a arreglar?
    """

    with open('nombre_piezas.txt', 'r', encoding='utf-8') as file:
        nombres = file.read().splitlines()
        return [Pieza(x, 100) for x in nombres]


def definir_estado_piezas(auto):
    """
    Método para definir el estado de las piezas
    """
    piezas = [pieza._replace(estado=uniform(0, 99)) for pieza in auto.piezas]
    auto.piezas = piezas
