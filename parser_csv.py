#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 20:02:34 2018

@author: Ruman

Se va a considerar un programa que permita:

Encontrar todos los archivos CSV del directorio actual.
Leer el contenido de cada archivo.
Escribir nuevamente el contenido saltándose la primera línea sobre un nuevo archivo CSV.
"""

import csv,re
from os import listdir

workdir="datos"
destfile=workdir+"/"+"parser.csv"

#lectura del directorio completo
ficheros=listdir(workdir)
#expresión regular para quedarme con una lista de .csv
r = re.compile(".*.csv")
ficheros_csv = list(filter(r.match, ficheros)) # Read Note

#creamos el writer
fichero_destino=open(destfile,"x")
fichero_destino=open(destfile,"a")
escritor=csv.writer(fichero_destino)

for listado in ficheros_csv:
    #Lectura del contenido de cada fichero
    print(workdir+"/"+listado)
    f=open(workdir+"/"+listado)  
    lector=csv.reader(f)
    #contenido
    contenido=list(lector)
    escritor.writerows(contenido[1:])



