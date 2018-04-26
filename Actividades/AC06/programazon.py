"""
-- programazon.py --

El módulo de Programazon cuenta con tres clases:
- TiendaFísica,
- TiendaOnline,
- Cliente.
"""

import hashlib
import random
import time
# import decoradores


class TiendaFísica:

    def __init__(self, dirección, jefe_tienda):
        self.dirección = dirección
        self.jefe_tienda = jefe_tienda

    def __repr__(self):
        return 'Programazon @ {}'.format(self.dirección)


class TiendaOnline:

    def __init__(self, sitio_web):
        self.sitio_web = sitio_web
        self.productos = {}

    def cargar_productos(self, filepath):
        for ítem in self._leer_archivo(filepath):
            self.productos.update(ítem)

    def __repr__(self):
        return 'Programazon ({})'.format(self.sitio_web)

    def _leer_archivo(self, filepath):
        with open(filepath, mode='r', encoding='UTF-8') as archivo:
            for línea in archivo:
                nombre, precio = self._procesar(línea)
                yield {nombre: int(precio)}

    @staticmethod
    def _procesar(línea):
        return línea.rstrip('\n').split(';')


class Cliente:

    def __init__(self, nombre, usuario, contraseña):
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = self._aplicar_hash(contraseña)

        self.saldo = 0
        self.carro = []

    def abonar(self, monto):
        self.saldo += monto
        self._mostrar_saldo()
        return self.saldo

    def agregar_al_carro(self, tienda, productos):
        for ítem in productos:
            if ítem not in tienda.productos:
                print("El producto '{}' no existe.".format(ítem))
            else:
                print("El producto '{}' ha sido agregado.".format(ítem))
                self.carro.append(ítem)

        print()
        return self.carro

    def pagar(self, tienda, contraseña):
        if not self.carro:
            print("El carro está vacío.")
            return False

        if self.contraseña != self._aplicar_hash(contraseña):
            print("Contraseña inválida.")
            return False

        latencia = random.uniform(2, 5)
        time.sleep(latencia)
        total = sum(tienda.productos[ítem] for ítem in self.carro)

        if self.saldo < total:
            print("Falta dinero, amigue.")
            return False

        print("Compra satisfactoria.")
        self.carro = []
        self.abonar(-total)

        return True

    def __repr__(self):
        return '{} (@{})'.format(self.nombre, self.usuario)

    def _mostrar_saldo(self):
        print("Saldo: {:,} CLP.".format(self.saldo))

    @staticmethod
    def _aplicar_hash(contraseña):
        return hashlib.sha1(str.encode(contraseña)).hexdigest()


if __name__ == '__main__':
    programazon_sj = TiendaOnline('https://sanjoaquin.programazon.cl')
    programazon_sj.cargar_productos('productos.csv')

    guido = Cliente('Guido van Rossum', 'guido', 'vanrossum123')
    guido.agregar_al_carro(programazon_sj, ['libro', 'manzana'])
    print(guido.saldo, guido.carro)

    guido.abonar(600)
    guido.pagar(programazon_sj, 'vanrossum123')
    guido.abonar(440)
    guido.pagar(programazon_sj, 'vanrossum123')
    print(guido.saldo, guido.carro)
