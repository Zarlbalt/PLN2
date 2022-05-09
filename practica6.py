
carpeta_nombre="C:\\Users\\cabap\\Documents\\Personal\\python\\documentos\\"
archivo_nombre="documento2.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto = archivo.read()

simbolo=["(",")",",",".",";",":","\","]

for simbolo in simbolo:
    texto=texto.replace(simbolo," " + simbolo + " ")

palabras_listas=texto.split()

palabras_unicas=[]

for palabra in palabras_listas:
    if palabra in palabras_unicas:
        continue
    palabras_unicas.append(palabra)
print(palabras_unicas)
num=len(palabras_unicas)
print("numero de palabras unicas en el documento:",num)
num2=len(palabras_listas)
print("numero de palabras en todo el documento:",num2)
