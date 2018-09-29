#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 19:29:46 2018

@author: Ruman
"""

#Opcion 2 
import csv 
archivo_csv=open("datos/prueba_5002.csv", "a")  
#es necesario crear un objeto de tipo writer  
escritor=csv.writer(archivo_csv)


#incluimos una linea
numero_caracteres=escritor.writerow(["prueba","prueba","prueba","prueba","","prueba"])
numero_caracteres=escritor.writerow(["prueba2","prueba2","prueba2","prueba2","","prueba2"])
numero_caracteres=escritor.writerow(["prueba2","prueba2","prueba2","prueba2","","prueba2,prueba3"])


#No es necesario cerrar el arcihivo para leerlo.
archivo_csv=open("datos/prueba_5002.csv", "r")  
lector=csv.reader(archivo_csv)
datos=list(lector)
print("La fina añadida es:", datos)

archivo_csv.close()


