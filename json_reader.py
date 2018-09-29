#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:19:00 2018

@author: Ruman
"""

import json 

#With, es una sentencia que proporciona mejor sintaxis y gestión de excenciones. Cierra automáticamente los archivos. 
with open('datos_json/colores.json', 'r') as f:
    quiz_dict = json.load(f)
    
#Devuelve un diccionario    
print ("Fichero_JSON Completo:",quiz_dict,"\n")
print ("Preguntas de  deporte;",quiz_dict["quiz"]["sport"],"\n")
print ("Preguntas de matemáticas;",quiz_dict["quiz"]["maths"],"\n")
print ("1ª Pregunta matemáticas;",quiz_dict["quiz"]["maths"]["q2"],"\n")

#Los tipos de datos JSON se corresponden con tipos de datos python.

print ("Los objetos JSON se representan en JSON como:", type(quiz_dict["quiz"]["maths"]["q2"]))
print ("Los objetos String se representan en JSON como:", type(quiz_dict["quiz"]["maths"]["q2"]["question"]))
print ("Los objetos Enteros se representan en JSON como:", type(quiz_dict["quiz"]["maths"]["q2"]["answer"]))
print ("Los objetos Enteros se representan en JSON como:", type(quiz_dict["quiz"]["maths"]["q2"]["answer_2"]))

