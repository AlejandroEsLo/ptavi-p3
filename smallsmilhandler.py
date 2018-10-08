#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar etiquetas SMIL
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.etiqueta = ""
        self.width = ""
        self.height = ""
        self.backgroundcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.dicc = []
    
    def startElement(self, etiqueta, attrs):
              
        if etiqueta == 'root-layout':
            # De esta manera tomamos los valores de los atributos
            self.etiqueta = etiqueta
           
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.backgroundcolor = attrs.get('background-color', "")
            self.data = self.width + self.height + self.backgroundcolor
            self.dicc = (etiqueta,self.width,self.height,self.backgroundcolor)
          
            print(self.dicc)
            
        elif etiqueta == 'region':
            
            self.etiqueta = etiqueta
            self.id = attrs.get('id', "")  
            self.top = attrs.get('top', "")
            self.left = attrs.get('left', "")
            self.dicc = (self.etiqueta,self.id,self.top,self.left)
            
            print(self.dicc)
            
    def get_tags(self):
       
       return self.dicc

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()#Creo parser
    cHandler = SmallSMILHandler()#Creo manejador
    parser.setContentHandler(cHandler)#Le paso el parser al manejador
    parser.parse(open('karaoke.smil'))#Leo lineas parseando
 #   print(cHandler.startElement(etiqueta,attrs))
    
    