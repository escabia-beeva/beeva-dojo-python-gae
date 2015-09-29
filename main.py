# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sesión 01 - Ejercicio 01

"""

from datetime import datetime

INICIO = 2000
FIN = 2397
FORMATO = '%d/%m/%Y %H:%M:%S:%f'


def get_fecha():
    return datetime.now()


def get_listado_multiplos():
    return sorted([i for i in range(INICIO, FIN) if i % 7 == 0], reverse=True)


def parse_to_string(my_list):
    return str(my_list).strip('[]').replace(',', ';').replace(' ', '')


def main():
    fecha = get_fecha()
    print '%s' % fecha.strftime(FORMATO)
    print '%s' % parse_to_string(get_listado_multiplos())
    fecha = get_fecha()
    print '%s' % fecha.strftime(FORMATO)

    exit(0)


if __name__ == '__main__':
    main()
