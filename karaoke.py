#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

import sys
import json

from urllib.request import urlretrieve
from smallsmilhandler import SmallSMILHandler

try:
    fich_smil = sys.argv[1]
    
    fich_json = sys.argv[1].replace(".smil",".json")
    
    parser = make_parser()
    my_class = SmallSMILHandler()
    parser.setContentHandler(my_class)
    parser.parse(open(fich_smil))
     
    with open(fich_json, "w") as fichToJson:    
    
        my_archv = my_class.get_tags()
        archv_smil = ""
        linea_final = ""
        for linea in my_archv:
            elementoX = linea[0]
            atributoXY = linea[1]
            
            #Iteramos por el archivo            
            for valorXY in atributoXY:
                if atributoXY[valorXY] != "":
                    elementoX += "\\t" + str(valorXY) + "=\"" + str(atributoXY[valorXY]) + "\""             
                
                linea_final = elementoX + "\\n"  
                
            archv_smil = archv_smil + linea_final + "\n"

            #Fichero final Json            
            json.dump(linea_final,fichToJson)

            #Descargamos archivos url http://            
            for valorXY in atributoXY:
                if valorXY == "src" and atributoXY[valorXY][:7] == "http://":
                    urlretrieve(atributoXY[valorXY], atributoXY[valorXY].split("/")[-1])
                    
                    atributoXY[valorXY] = atributoXY[valorXY].split("/")[-1]
                    
                    print("Descargando %s..." % atributoXY[valorXY])
                    
                
    print(archv_smil)
        
except IndexError:
    sys.exit("Usage:python3 karaoke.py file.smil.")
    
except FileNotFoundError:
    sys.exit("No existe el archivo introducido")
