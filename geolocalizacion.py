#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 19:12:27 2018

@author: Ruman
    Leer desde teclado una ciudad.
    Llamar a la API de geocodificación de Google.
    Extraer la información en formato JSON que nos devuelve.
"""

import signal, sys, requests

#Capturar control-c
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

#URL API REST GOOGLE MAPS
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


while True:
    print("Introduce una ciudad:")
    ciudad = input()
    req = requests.get(GOOGLE_MAPS_API_URL,{'address': ciudad, 'sensor': 'false', 'key':'AIzaSyAL48U7mrfXRauM5Z5wV_r1M08rN8qRA-Y'})
    #req.json() Present in requests.models.Response module
    res = req.json()
    print (res["results"][0]["geometry"]["location"])


    


