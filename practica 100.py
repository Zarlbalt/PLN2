"""Carlos Alejandro Baltazar Padilla"""
import os

carpeta_nombre="C:\\Users\\cabap\\Documents\\Personal\\python\\documentos\\"

archivos_listados=os.listdir(carpeta_nombre)
for archivo_nombre in archivos_listados:
    print(archivo_nombre)
    archivo = open(carpeta_nombre+archivo_nombre)
    lineas_lista = archivo.readlines()
    archivo.close()
    longitud = len(lineas_lista)
    print("El archivo", archivo_nombre,"tiene",longitud,"lineas")

    archivo = open(carpeta_nombre+archivo_nombre)
    texto = archivo.read()
    archivo.close()

    simbolo=["(",")",",",".",";",":","\","]
    for simbolo in simbolo:
        texto=texto.replace(simbolo," " + simbolo + " ")
    
    palabras_listas=texto.split()
    palabras_listas.sort()
    for palabra in palabras_listas:
        print(palabra)

