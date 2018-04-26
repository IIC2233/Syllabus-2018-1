"""
-- testing.py --

El módulo que te ayudará a verificar unos pocos escenarios.
Es importante mencionar que aunque todas las pruebas pasen,
esto **no implica** que el programa funciona correctamente.
"""

import unittest
from programazon import TiendaOnline, Cliente


class MyTest(unittest.TestCase):

    def setUp(self):
        self.programazon_sj = TiendaOnline('https://sanjoaquin.programazon.cl')
        self.programazon_sj.cargar_productos('productos.csv')
        self.guido = Cliente('Guido van Rossum', 'guido', 'vanrossum123')
        self.productos = ['libro', 'laptop']

    def test_productos_agregados(self):
        """
        Test: “Lo que agregué al carro debería estar en el carro.”
        """
        self.assertEqual(
            self.guido.agregar_al_carro(self.programazon_sj, self.productos),
            self.productos
        )

    def test_no_tenemos_centavos(self):
        """
        Test: “En Chile, hace tiempo que no existen los centavos.”
        """
        with self.assertRaises(TypeError):
            self.guido.abonar(1234.56)


if __name__ == '__main__':
    unittest.main()
