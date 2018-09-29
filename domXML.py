#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 21:52:22 2018

@author: Ruman
"""

import xml.dom.minidom

#devuelve un <class 'xml.dom.minidom.Document'>
ArbolDOM = xml.dom.minidom.parse("datos_xml/orders.xml")

#acceso a la raiz del arbol
raiz = ArbolDOM.documentElement;
print ("Raiz del documento:",raiz)

#devuelve una lista con los elementos cuyo nombre coincide con el indicado
direcciones = ArbolDOM.getElementsByTagName("address")
print(direcciones)

#for lista in direccion:
for direccion in direcciones:
    #Revisar si tiene el atributo Type y pintarlo
    if direccion.hasAttribute("type"):
        print ("Atrubuto:",direccion.getAttribute("type"))
    
    print ("Dirección:", direccion.childNodes[0].data)
    
    



