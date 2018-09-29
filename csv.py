# -*- coding: utf-8 -*-
"""
Programa de prueba para manejo de ficheros CSV.
"""
"""
import csv
archivo_csv=open("datos/prueba_5000.csv")

#es necesario crear un objeto de tipo reader
lector=csv.reader(archivo_csv)

for fila in lector:
    print("Linea#", lector.line_num, str(fila))
    
#El objeto Reader solo puede ser recorrido una única vez, 
#de forma que si se quiere volver a hacerlo habría que usar nuevamente el método csv.reader.
"""
      
#Opcion 2 
import csv 
archivo_csv=open("datos/prueba_5000.csv")  
#es necesario crear un objeto de tipo reader  
lector=csv.reader(archivo_csv)
contenido=list(lector)
print("Primera Fila:", contenido[0], "\n")
print("Ultima Fila:", contenido[-1], "\n")
print("Segundo elemento de la primera fila:", contenido[0][1])
