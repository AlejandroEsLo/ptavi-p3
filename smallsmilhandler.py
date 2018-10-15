#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        # Creamos listas con sus correspondientes atributos
        self.rootlayout = ["width", "height", "background-color"]
        self.region = ["id", "top", "bottom", "left", "right"]
        self.img = ["src", "region", "begin", "dur"]
        self.audio = ["src", "begin", "dur"]
        self.textstream = ["src", "region"]

        # Lista vacia para ir almacenando las listas anteriores al rellenarse
        self.data = []

    def startElement(self, etiqueta, attrs):

        # Creamos un diccionario con la etiqueta y sus atributos
        self.dicc = {"root-layout": self.rootlayout, "region": self.region,
                     "img": self.img, "audio": self.audio,
                     "textstream": self.textstream}

        dicc_aux = {}

        if etiqueta in self.dicc:
            # Iteramos por todos los atributos de cada etiqueta
            for attrb in self.dicc[etiqueta]:
                dicc_aux[attrb] = attrs.get(attrb, "")

            # Añadir al final de la lista
            self.data.append([etiqueta, dicc_aux])

    def get_tags(self):

        return self.data


if __name__ == "__main__":

    parser = make_parser()  # Creo parser
    cHandler = SmallSMILHandler()  # Creo manejador
    parser.setContentHandler(cHandler)  # Le paso el parser al manejador
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
