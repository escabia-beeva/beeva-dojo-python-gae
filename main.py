__author__ = 'escabia'

from random import randint
from agentes import Criminal
from agentes import Chivato
from cazarrecompensas import Captura
from cazarrecompensas import Cazarrecompensas
from operator import attrgetter
import sys
import names

DIAS = 7
HORA_INICIAL = 8
HORA_FIN = 22
HORAS_POR_DIA = HORA_FIN - HORA_INICIAL
TIEMPO_TOTAL = DIAS * HORAS_POR_DIA
EUROS_POR_PUNTO_DE_VIDA_CRIMINAL = 30
GASTO_POR_DISTANCIA = 3
LIMITE_DE_PUNTOS_VIDA_CRIMINAL = 10
LIMITE_CRIMINALES_CHIVATO = 10
DISTANCIA_MAXIMA = 20
MIN_NUM_CHIVATOS = 1
MAX_NUM_CHIVATOS = 10

if(len(sys.argv) > 5):
    EUROS_POR_PUNTO_DE_VIDA_CRIMINAL = int(sys.argv[1])
    GASTO_POR_DISTANCIA = int(sys.argv[2])
    LIMITE_DE_PUNTOS_VIDA_CRIMINAL = int(sys.argv[3])
    LIMITE_CRIMINALES = int(sys.argv[4])
    DISTANCIA_MAXIMA = int(sys.argv[5])

else:
    print "No se ha ejecutado el programa con los argumentos, se definiran los siguientes valores por defecto: "
    print "EUROS_POR_PUNTO_DE_VIDA_CRIMINAL: " + str(EUROS_POR_PUNTO_DE_VIDA_CRIMINAL)
    print "GASTO POR DISTANCIA " + str(GASTO_POR_DISTANCIA)
    print "LIMITE_DE_PUNTOS_VIDA_CRIMINAL: " + str(LIMITE_DE_PUNTOS_VIDA_CRIMINAL)
    print "LIMITE_CRIMINALES POR CHIVATO: " + str(LIMITE_CRIMINALES_CHIVATO)
    print "DISTANCIA_MAXIMA: " + str(DISTANCIA_MAXIMA)
    print "\n"


def inicializar_datos_chivatos():
    for i in range(1,randint(MIN_NUM_CHIVATOS, MAX_NUM_CHIVATOS)):
        if randint(0,1) == 1:
            posibles_chivatos.append(Criminal(names.get_full_name(),randint(1,DISTANCIA_MAXIMA),randint(1,LIMITE_DE_PUNTOS_VIDA_CRIMINAL)))
        else:
            chivato = Chivato(randint(1,DISTANCIA_MAXIMA))
            for j in range(1,randint(2,LIMITE_CRIMINALES_CHIVATO)):
                chivato.criminales.append(Criminal(names.get_full_name(),randint(1,DISTANCIA_MAXIMA),randint(1,LIMITE_DE_PUNTOS_VIDA_CRIMINAL)))
            posibles_chivatos.append(chivato)

def almacenaCaptura(agente):
    cazarrecompensas.capturas.append(Captura(TIEMPO_TOTAL,agente))
    cazarrecompensas.gastos += agente.distancia * GASTO_POR_DISTANCIA
    cazarrecompensas.ingresos += agente.vida * EUROS_POR_PUNTO_DE_VIDA_CRIMINAL

posibles_chivatos = []
inicializar_datos_chivatos()
posibles_chivatos_ordenados = sorted(posibles_chivatos, key=attrgetter('distancia'), reverse=False)
criminales_a_visitar = []
cazarrecompensas = Cazarrecompensas(HORAS_POR_DIA, HORA_INICIAL)

for posible_chivato in posibles_chivatos_ordenados:
    if isinstance(posible_chivato, Criminal) and TIEMPO_TOTAL >= int(posible_chivato.vida):
        TIEMPO_TOTAL -= posible_chivato.vida
        if TIEMPO_TOTAL > 0:
            almacenaCaptura(posible_chivato)
    else:
        if hasattr(posible_chivato, 'criminales'):
            cazarrecompensas.gastos += posible_chivato.distancia * GASTO_POR_DISTANCIA
            criminales_del_chivato = sorted(posible_chivato.criminales, key=attrgetter('distancia'), reverse=False)
            for criminal in criminales_del_chivato:
                TIEMPO_TOTAL -= criminal.vida
                if TIEMPO_TOTAL > 0:
                    almacenaCaptura(criminal)

cazarrecompensas.display()

















