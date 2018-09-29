#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:42:09 2018

@author: Ruman
"""

from xml.etree import ElementTree

fichero = open("datos_xml/libros.xml")

for (event, element) in ElementTree.iterparse(fichero,('start','end')):
    if event == "start":
        if element.tag == "Libro":
            print (element.tag, element.attrib)
    if event == "end":
        print (element.text)