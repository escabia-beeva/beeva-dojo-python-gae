#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'escabia'


class Criminal:

    def __init__(self, nom, distancia, vida):
        self.nom = nom
        self.distancia = distancia
        self.vida = vida


class Chivato:

    def __init__(self, distancia):
        self.distancia = distancia
        self.criminales = []
