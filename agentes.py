__author__ = 'escabia'


class Criminal:

    def __init__(self, nom, distancia, vida):
        self.nom = nom
        self.distancia = distancia
        self.vida = vida

    def display(self):
        return self.nom


class Chivato:

    def __init__(self, distancia):
        self.distancia = distancia
        self.criminales = []

    def output(self):
        return "Chivato: " + str(self.distancia) + " criminal: " + self.criminal.output()
