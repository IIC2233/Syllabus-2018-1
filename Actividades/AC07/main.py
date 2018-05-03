#################################
#  NO MODIFICAR CODIGO DE ABAJO #
#################################

__author__ = "Tomas Rivera, Rodrigo Hanuch"
# -*- coding: utf-8 -*-

from metaclases import MetaAuto, MetaTrabajador


class Auto(metaclass=MetaAuto):
    '''
    Auto en si mismo
    '''

    def __init__(self, *args, **kwargs):
        pass


class Trabajador(metaclass=MetaTrabajador):
    '''
    Trabajador en si mismo, sólo puede ser instanciado una vez.
    '''

    def __init__(self):
        pass

    def revizar_ztado(self):
        pass

    # def repair(self, car):
    #     pass


##########################################
#  NO MODIFICAR CODIGO DE ARRIBA Y ABAJO #
##########################################

if __name__ == "__main__":

    # Instanciando clases
    auto = Auto()
    auto2 = Auto()
    auto3 = Auto()
    auto4 = Auto()
    trabajador = Trabajador()
    trabajador2 = Trabajador()

    # Verificando que estás en lo correcto
    if trabajador is trabajador2 and trabajador2 is not None:
        print("OK. El trabajador ha sido instanciado una sola vez!\n")
    else:
        print("¡Alerta! La clase Trabajador ha sido instanciada dos veces!")
        print("Recuerda que es un taller pequeño, atendido por su dueño, y sin empleados.\n")

    try:
        trabajador.revizar_ztado()
        print("¡Alerta! NO se ha eliminado revizar_ztado.")
        print("Zí nô mé kàmviâz nò bóì â pódèr bólbèr âl kárrêtè\n")
    except AttributeError:
        print("OK. El método revizar_ztado fue eliminado.\n")

    try:
        trabajador.revisar_estado(auto)
        print("OK. El método revisar_estado ha sido agregado.\n")
    except AttributeError:
        print("¡Alerta! El método revisar_estado NO ha sido agregado.")
        print("Y tho?\n")

    try:
        if trabajador.reparar:
            print("OK. El método reparar ha sido agregado.\n")
    except AttributeError:
        print("¡Alerta! El método reparar NO ha sido agregado.")
        print("Algún día lo repararás... yo sé que en el fondo quieres.\n")

    try:
        if isinstance(auto.piezas, list):
            print("OK. El auto tiene una lista de piezas!\n")
    except AttributeError:
        print("¡Alerta! El auto NO tiene una lista de piezas.")
        print("¿Cómo llegué aquí? ._.\n")

    try:
        if auto.definir_estado_piezas:
            print("OK. El método definir_estado_piezas fue agregado.\n")
    except AttributeError:
        print("¡Alerta! El método definir_estado_piezas NO fue agregado.")
        print("¿Cómo pretendes que las piezas sean reales si no tienen un estado? :O\n")

    try:
        if auto.piezas[0].nombre == "Volante de dirección":
            print("OK. Los nombres de las piezas fueron asignados.\n")
    except AttributeError:
        print("¡Alerta! Los nombres de las piezas NO fueron asignados.")
        print("¡No dejes que todas las piezas sean iguales! Todos somos únicos :( \n")

    try:
        if Auto.piezas[0].estado != auto.piezas[0].estado:
            print("OK. El estado de las piezas fue asignado.\n")
    except AttributeError:
        print("¡Alerta! El estado de las piezas NO fue asignado.")
        print("¡Debes imponer orden!\n")

    cdt = all(isinstance(auto, Auto)
              for auto in [auto, auto2, auto3]) and auto4 is None
    if cdt:
        print("OK. Se instació el número correcto de autos.\n")
    if not cdt:
        print("¡Alerta! NO se instació el número correcto de autos")
        print("¡Cuidado con que explote alguno!\n")

    try:
        auto.piezas[0].nombre
        print("OK. El atributo nombre fue agregado\n")
    except AttributeError:
        print("¡Alerta! El atributo nombre NO fue agregado.")
        print("Oe yapo...¡corrígeme!\n")

    try:
        auto.piezas[0].estado
        print("OK. El atributo estado fue agregado.\n")
    except AttributeError:
        print("¡Alerta! El atributo estado NO fue agregado.")
        print("Un byte perdio a su familia por no agregarlo :(\n")

    # Arreglando tu auto (V)(°,,,,°)(V)
    try:
        trabajador.revisar_estado(auto)
        trabajador.reparar(auto)
        trabajador.revisar_estado(auto)
    except AttributeError as e:
        print("¡Alerta! Hasta ahora {}. ¡Corrígelo!".format(e))

##################################
#  NO MODIFICAR CODIGO DE ARRIBA #
##################################
