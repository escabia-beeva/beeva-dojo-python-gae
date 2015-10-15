#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'escabia'

from operator import attrgetter

DIAS = [
    "Lunes",
    "Martes",
    "Miercoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo"
]


class Cazarrecompensas:

    def __init__(self, horasdia, horacomienzo):
        self.horasdia = horasdia
        self.horacomienzo = horacomienzo
        self.ingresos = self.gastos = 0
        self.capturas = []

    def display(self):
        capturas_realizadas = sorted(self.capturas, key=attrgetter('hora'), reverse=False)

        if(len(capturas_realizadas) > 0):
            captura = capturas_realizadas.pop()
            for dia in DIAS:
                print "\n" + dia + "\n"
                for i in range(self.horacomienzo, self.horasdia + self.horacomienzo):
                    if captura.criminal.vida == 0:
                        print str(i) + " h" + " " + captura.criminal.nom + " capturado"
                        if len(capturas_realizadas) > 0:
                            captura = capturas_realizadas.pop()
                        else:
                            print "SERVICIOS REALIZADOS -> CRIMINALES CAPTURADOS"
                    else:
                        if captura.criminal.vida > 0:
                            print str(i) + " h" + " " + captura.criminal.nom + " " + str(captura.criminal.vida) + "pv"
                        else:
                            print str(i) + " h" + " VACACIONES"
                    captura.criminal.vida -= 1

            print "\nReconpensa total: " + str(self.ingresos) + "\xe2\x82\xac\nGastos totales: " + str(self.gastos) +"\xe2\x82\xac"

            for captura in capturas_realizadas:
                print str(captura.hora) + captura.criminal.display()


class Captura:
    def __init__(self, hora, criminal):
        self.hora = hora
        self.criminal = criminal