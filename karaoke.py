#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from smallsmilhandler import SmallSMILHandler
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import json
from urllib.request import urlretrieve  # En python2 sin .request


class KaraokeLocal():

    def __init__(self, fich):
        parser = make_parser()
        my_class = SmallSMILHandler()
        parser.setContentHandler(my_class)
        parser.parse(open(fich_smil))
        self.my_archv = my_class.get_tags()

    def __str__(self):
        archv_smil = ""
        linea_final = ""
        for linea in self.my_archv:
            elementoX = linea[0]
            atributoXY = linea[1]

            # Iteramos por el archivo
            for valorXY in atributoXY:
                if atributoXY[valorXY] != "":
                    elementoX += "\\t" + str(valorXY) + "=\"" + str(atributoXY[valorXY]) + "\""

                linea_final = elementoX + "\\n"

            archv_smil = archv_smil + linea_final + "\n"

        print(archv_smil, end="")  # Imprimimos archivo smil
        # Utilizamos el "end" para quitar el ultimo salto de linea

    def to_json(self, fich_json):
        # Fichero final Json
        json.dump(self.my_archv, open(fich_json, "w"))

    def do_local(self):
        # Descargamos archivos url http://
        for valorXY in self.my_archv:
            atributoXY = valorXY[1]
            for valorXY in atributoXY:
                if valorXY == "src" and atributoXY[valorXY][0:7] == "http://":
                    urlretrieve(atributoXY[valorXY],
                                atributoXY[valorXY].split("/")[-1])

                    atributoXY[valorXY] = atributoXY[valorXY].split("/")[-1]
                    # Prueba para ir viendo que va descargando...
                    # print("Descargando %s..." % atributoXY[valorXY])


if __name__ == "__main__":

    # Programa principal
    try:
        fich_smil = sys.argv[1]  # Fichero principal
        fich_json = sys.argv[1].replace(".smil", ".json")  # Fichero Json
        fich_karaoke = KaraokeLocal(fich_smil)
        fich_karaoke.__str__()
        fich_karaoke.to_json(fich_json)  # Pasamos fichero smil a fichero Json
        fich_karaoke.do_local()  # Descargamos archivos

    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")

    except FileNotFoundError:
        sys.exit("No existe el archivo introducido")
