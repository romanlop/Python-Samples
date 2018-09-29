#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:29:01 2018

@author: Ruman
"""

import xml.sax

#En Python a la hora de utiliza herencia, la fase padre se indica dentro del paréntesis de la clase que vas a definir. 
class ManejadorXML (xml.sax.ContentHandler):
    
#El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método. 
#Es decir, el objeto que usaste para llamar al método   
    def __init__(self):
        #xml.sax.ContentHandler.__init__(self)
        self.etiqueta=""
   
    
    def startElement(self, nombre, attrs):
        #print("startElement '" + nombre + "'")
        self.etiqueta=nombre;
        if nombre == "address":
          print("\tattribute type='" + attrs.getValue("type") + "'") #type es el nombre del atributo en el XML
    
    def endElement(self, nombre):
        #print("endElement '" + nombre + "'")
        pass
        
    def characters(self, contenido):
        if self.etiqueta=="address":
            if contenido != "\n":
                print(self.etiqueta + contenido)  
    
    
def main(sourceFileName):
  source = open(sourceFileName)
  xml.sax.parse(source, ManejadorXML())


main("datos_xml/orders.xml")  
  
"""
Merece la pena señalar aquí la implementación de startElement. 
Esto se invoca a cada elemento en el documento fuente que se encuentra. 
Solo el elemento de dirección tiene atributos, 
por lo que hay una comprobación explícita para esta etiqueta de elemento antes de intentar acceder al valor del atributo de tipo.
"""