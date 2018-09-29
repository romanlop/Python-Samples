#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 13:12:15 2018

@author: Ruman
"""

from xml.etree.ElementTree import Element,SubElement,Comment,tostring
from xml.etree import ElementTree as ET
from xml.dom import minidom

def pretty(elem):
    cadena = tostring(elem,'utf-8')
    #este método lo pasa a minidom para luego aplicar el prettyxml -> identar.
    bonito = minidom.parseString(cadena)
    cadena_final = bonito.toprettyxml(encoding='utf-8')
    #pasamos de Bytes a cadena para luego guardar en fichero
    return cadena_final.decode('utf-8')
    


raiz=Element("catalogo")
#Los atributos se pasan como un diccionario
Libro=SubElement(raiz,"Libro",{"orden":"1"})
Titulo=SubElement(Libro,"Titulo")
Titulo.text="El Quijote"


contenido=pretty(raiz)

fichero= open ("datos_xml/salida.xml",'x')
fichero.write(contenido)
fichero.close()







