from asyncore import read


print("Procesamiento de lenguaje natural")
print("Ingenieria en la computacion")

suma = 7+5
resultado= suma*6
print("Resultado: ",resultado)

print("___________________________________")

archivo = open("C:\\Users\\cabap\\Documents\\Personal\\python\\documento.txt","r")


print(archivo.read())
archivo2 = open("C:\\Users\\cabap\\Documents\\Personal\\python\\documenton.txt", "w")
cadena1="Primera clase de programacion python"
archivo2.write(cadena1)
archivo2 = open("C:\\Users\\cabap\\Documents\\Personal\\python\\documenton.txt")
print(archivo2.read())
archivo2.close()



carpeta_nombre="C:\\Users\\cabap\\Documents\\Personal\\python\\"
archivo_nombre="acuerdo.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    lineas_lista=archivo.readlines()

num_linea=1

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


with oopen(carpeta_nombre+ archivo_nombre,"r") as archivo:
    texto=archivo.read()
if palabra1 in texto:
    Print("el texto de lo que esta esta bien",palabra2)