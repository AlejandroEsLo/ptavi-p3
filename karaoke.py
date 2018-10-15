#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import json
from urllib.request import urlretrieve
from smallsmilhandler import SmallSMILHandler

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
            
            #Iteramos por el archivo            
            for valorXY in atributoXY:
                if atributoXY[valorXY] != "":
                    elementoX += "\\t" + str(valorXY) + "=\"" + str(atributoXY[valorXY]) + "\""             
                
                linea_final = elementoX + "\\n"  
                
            archv_smil = archv_smil + linea_final + "\n"
        
        print(archv_smil)
              
if __name__ == "__main__":   
#Programa principal
    try:
        fich_smil = sys.argv[1]
        fich_karaoke = KaraokeLocal(fich_smil)     
        fich_karaoke.__str__()
      
        print("SALIDA(PRUEBA)")
        
        
    except IndexError:
        sys.exit("Usage:python3 karaoke.py file.smil.")
        
    except FileNotFoundError:
        sys.exit("No existe el archivo introducido")
