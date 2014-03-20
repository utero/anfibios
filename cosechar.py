#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
import codecs
import sys


def request(filename):
    import os.path
    if os.path.isfile(filename):
        f = codecs.open(filename, "r", "utf8")
        lines = f.readlines()
        f.close()
        for i in lines:
            i = i.strip().split(",")
            especie = i[0]
            if especie == "Especie":
                continue

            print especie
    else:
        print "No se pudo encontrar ese archivo"
        print "Nada por hacer"

def main():
    description = """Este script extrae coordenadas geográficas de iNaturalis
    para una lista de especies."""

    parser = argparse.ArgumentParser(description=description,formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--filename', action='store',
            metavar='Lista_de_especies.csv',
            help='''Nombre de las especies en archivo formato de texto. Una
            especie por línea.''',
            required=True, dest='filename')

    args = parser.parse_args()
    filename = args.filename.strip()

    request(filename)


if __name__ == "__main__":
    main()
