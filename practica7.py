import re
carpeta_nombre="C:\\Users\\cabap\\Documents\\Personal\\python\\documentos\\"
archivo_nombre="documento2.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

expresion_regular=re.compile(r"la")

resultados_busqueda=expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))

"""Practica 8 """
expresion_regular=re.compile(r".*")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado3 in resultados_busqueda:
    print(resultado3.group(0))

expresion_regular=re.compile(r"ha+")
resultados_busqueda=expresion_regular.finditer(texto)
for resultado4 in resultados_busqueda:
    print(resultado4.group(0))