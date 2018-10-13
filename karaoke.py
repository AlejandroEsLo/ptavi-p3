#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import json

from smallsmilhandler import SmallSMILHandler

try:
    my_class = SmallSMILHandler()
    
    fich_smil = sys.argv[1]
    
    fich_json = sys.argv[1].replace(".smil",".json")
    
    parser = make_parser()
    my_class = SmallSMILHandler()
    parser.setContentHandler(my_class)
    parser.parse(open(fich_smil))
    with open(fich_json, "w") as fichToJson:
    
    
        my_archv = my_class.get_tags()
    
        linea_final = ""
        for linea in my_archv:
            elementoX = linea[0]
            atributoXY = linea[1]
            
            for valorXY in atributoXY:
                if atributoXY[valorXY] != "":
                    elementoX += "\\t" + str(valorXY) + "=\"" + str(atributoXY[valorXY]) + "\""             
                
                linea_final = elementoX + "\\n"       
    
            json.dump(linea_final,fichToJson)
            
            print(linea_final)
        
except IndexError:
    sys.exit("Usage:python3 karaoke.py file.smil.")
    
except FileNotFoundError:
    sys.exit("No existe el archivo introducido")
