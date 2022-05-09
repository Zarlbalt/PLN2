carpeta_nombre="C:\\Users\\cabap\\Documents\\Personal\\python\\"
archivo_nombre="acuerdo.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

num_linea=1