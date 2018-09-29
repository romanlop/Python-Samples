#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:57:25 2018

@author: Ruman
"""

from xml.etree import ElementTree

fichero = open("datos_xml/libros2.xml")
arbol = ElementTree.parse(fichero)

#añadir nuevo atributo
i=1
for nodo in arbol.iter("Libro"):
    print (nodo.tag, nodo.text)
    nodo.set('Orden',str(i))
    #Añadimos un nuevo elemento
    editorial=ElementTree.Element("editorial")
    editorial.text="Anaya"
    nodo.append(editorial)
    i=i+1
    
arbol.write("datos_xml/modificado.xml")
            
            

