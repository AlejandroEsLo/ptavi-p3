#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__ (self):

        #Creamos listas con sus correspondientes atributos
        self.rootlayout = ["width","height","background-color"]
        self.region = ["id","top","bottom","left","right"]
        self.img = ["src","region","begin","dur"]
        self.audio = ["src","begin","dur"]
        self.textstream = ["src","region"]
        
        #Lista vacia para ir almacenando las listas anteriores al rellenarse
        self.data = []
    
    def startElement(self, etiqueta, attrs):

        #Creamos un diccionario con la etiqueta y su atributo correspondiente
        self.dicc = {"root-layout": self.rootlayout, "region": self.region,
                     "img": self.img, "audio": self.audio,
                     "textstream": self.textstream}

#        dicc_aux ={}  >> ir almacenando

        if etiqueta in self.dicc:

            self.data.append(etiqueta)# Añadir al final de la lista
      
    def get_tags(self):
       
       return self.data

if __name__ == "__main__":

    parser = make_parser()#Creo parser
    cHandler = SmallSMILHandler()#Creo manejador
    parser.setContentHandler(cHandler)#Le paso el parser al manejador
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
    
    