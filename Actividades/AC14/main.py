import re
import random

from config import USERNAME, PASSWORD

### REGEX

def validar_correo(correo):
    """
    Retorna True si el formato del correo es valido y si el servidor existe,
    en otro caso retorna False
    :param correo: str
    :return: bool
    """
    pass


def arreglar_memes(path, pathfinal):
    """"
    Abre el archivo path y corrige cada una de las solicitudes del enunciado
    guardándolas en pathfinal
    :param path: str
    :param pathfinal: str
    :return:
    """
    pass


### Web Services

def obtener_mejores():
    """
    Retorna una muestra aleatoria de 10 memes provenientes de los 100 mejores
    :return: [dict]
    """
    pass

def generar_meme(template_id, username, password, text0, text1):
    """
    Genera un meme correspondiente al template_id con texto superior text0
    y texto inferior text1. Retorna la url al meme
    :param template_id: int
    :param username: str
    :param password: str
    :param text0: str
    :param text1: str
    :return: str
    """
    pass

def menu():
    correo = input("Ingrese correo: ")
    while not validar_correo(correo):
        correo = input("Ingrese correo: ")

    on = True
    while on:
        print("""[1] Ver 10 de los mejores memes
[2] Generar meme
[3] Ver meme del archivo""")
        opcion = input("Que quieres hacer? ")
        while opcion not in ["1", "2", "3"]:
            opcion = input("Que quieres hacer? ")

        if opcion == "1":
            i = 1
            print("\n10 de los mejores memes son:")
            for meme in obtener_mejores():
                print(f"[{i}] template_id: {meme['id']}\nnombre: {meme['name']}\n"
                      f"url: {meme['url']}\n")
                i += 1
        elif opcion == "2":
            template_id = input("Ingrese template_id: ")
            text0 = input("Ingrese texto superior: ")
            text1 = input("Ingrese texto inferior: ")
            url = generar_meme(template_id, USERNAME, PASSWORD, text0, text1)
            print(f"\nPuedes ver tu meme aqui: {url}")
        elif opcion == "3":
            with open('arreglados.txt', 'r', encoding = 'utf-8') as m:
                memes = dict()
                numero = 1
                for linea in m:
                    memes[str(numero)] = (linea.strip().split(','))
                    numero += 1
            print("Escoja meme para ver: ")
            for meme in memes:
                print("[{}] TEXTO SUPERIOR: {} || TEXTO INFERIOR: {}".format(meme,  memes[meme][1], memes[meme][2]))
            dec = input("¿Cual desea ver?")
            if memes.get(dec) != None:
                url = generar_meme(memes[dec][0], USERNAME, PASSWORD, memes[dec][1], memes[dec][2])
                print(f"\nAquí va el meme: {url}")


if __name__ == "__main__":
    #arreglar_memes("memes.txt", "arreglados.txt")
    menu()
