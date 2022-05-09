carpeta_nombre="C:\\Users\\cabap\\Documents\\Personal\\python\\"
archivo_nombre="acuerdo.txt"
palabra1="acuerdo"
palabra2="RESOLUCION"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
if palabra1 in texto:
    print("El documento es un(a)", palabra1)
elif palabra2 in texto:
    print("El documento es un(a)", palabra2)
else:
    print("El documento no es un ACUERDO ni una RESOLUCION")