#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:13:04 2018

@author: Ruman
"""

from xml.etree import ElementTree

fichero = open("datos_xml/libros.xml")
#parseamos el documento. Se genera un objeto de tipo ElementTree
arbol = ElementTree.parse(fichero)

print ("***********************************") 
print ("Contenido del XML:")
for nodo in arbol.iter():
    #pintamos algunos de los atributos de cada elemento del iterador
    print (nodo.tag, nodo.attrib, nodo.text)
  
print ("***********************************") 
print ("\nLibros contenidos en el XML:") 
i=1
for nodo in arbol.iter("Libro"):
    #pintamos algunos de los atributos de cada elemento del iterador
    isbn=nodo.attrib.get("isbn")
    print ("Libro ",i, "Isbn", isbn)
    i=i+1

print ("***********************************") 
print ("\nPrimera Aparción de Libro:")    
for nodo in arbol.find("Libro"):
    #find devuelve el elemento completo con todos sus hijos. No cualquier elemento es iterable. 
    print (nodo.tag, nodo.text)

print ("***********************************") 
print ("\nTodas las apariciones de Libro:")    
for nodo in arbol.findall("Libro"):
    #devuelve todas las apariciones, pero no sus hijos.
    print (nodo.tag, nodo.attrib)