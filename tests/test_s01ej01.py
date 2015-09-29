import unittest
from unittest import TestCase
from datetime import datetime
from main import get_listado_multiplos, get_fecha, parse_to_string


class TestSession(TestCase):

    def setUp(self):
        self.listado_multiplos = get_listado_multiplos()

    def test_listado_numeros(self):
        self.assertIsNotNone(self.listado_multiplos)

        for numero in self.listado_multiplos:
            self.assertTrue(numero % 7 == 0)

    def test_fecha_inicio(self):
        fecha = get_fecha()
        self.assertIsInstance(fecha, datetime)

    def test_fecha_fin(self):
        fecha = get_fecha()
        self.assertIsInstance(fecha, datetime)

    def test_resultado_cadena(self):
        mi_cadena = parse_to_string(self.listado_multiplos)

        # Como mi_cadena va a tener un elemento menos que el numero de
        # elementos que contiene la lista, sumamos una unidad
        self.assertTrue(len(self.listado_multiplos) == mi_cadena.count(';') + 1)

    def test_listado_ordenado(self):
        last = self.listado_multiplos[len(self.listado_multiplos) - 1]
        first = self.listado_multiplos[0]

        self.assertGreater(first, last)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
