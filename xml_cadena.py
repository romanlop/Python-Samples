#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:49:50 2018

@author: Ruman

También es posible procesar cadenas que representen un documento 
XML usando el método fromstring, 
que toma como argumento la cadena que representa el documento XML

"""
from xml.etree import ElementTree as ET

cadena = '''
    <catalogo>
        <Libro isbn="1111">
            <titulo>El quijote</titulo>
            <autor>Cervantes</autor>
            <precio>1200</precio>
        </Libro>
        <Libro isbn="2222">
            <titulo>El si de las Niñas</titulo>
            <autor>Fernando de Rojas</autor>
            <precio>1800</precio>
        </Libro>
        <Libro isbn="3333">
            <titulo>Historia de una escalera</titulo>
            <autor>Buero vallejo</autor>
            <precio>200</precio>
        </Libro>
    </catalogo>
'''

#Esto devuelve un <Element 'catalogo' at 0x117deea98>
doc=ET.fromstring(cadena)

for nodo in doc.findall("Libro"):
    #devuelve todas las apariciones, pero no sus hijos.
    print (nodo.tag, nodo.attrib)