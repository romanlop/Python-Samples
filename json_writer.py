#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 18:54:39 2018

@author: Ruman

Construir fichero JSON
"""

import json 


contenidoJSON={'alumno1':{'nombre':'roman', 'matriculado':True, 'asignaturas':34, 'ID': None},
               'alumno2':{'nombre':'juan', 'matriculado':False, 'asignaturas':34, 'ID': None}}

with open('datos_json/alumnos.json', 'x') as outfile:
    json.dump(json.dumps(contenidoJSON), outfile)



with open('datos_json/alumnos.json', 'r') as infile:
    alumnos = json.load(infile)
    print(alumnos)


