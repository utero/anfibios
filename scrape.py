#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from argparse import RawTextHelpFormatter
import sys


def scrape(filename):
    import os.path
    if os.path.isfile(filename):
        print "good"
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

    scrape(filename)


if __name__ == "__main__":
    main()
