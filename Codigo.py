"""
Creador: Carlos Alejandro Baltazar Padilla
Maestro: Carrillo Zepeda Oswaldo
Materia: Procesamiento de Lenguaje Natural

Puntos para elaborar:
    - El programa consiste en leer dos documentos de texto .txt               **
    - De los cuales muestre cuantas líneas (longitud) con texto y             **
    - Cada documento de texto debe de tener tres párrafos como mínimo.        **
    - Cuantas líneas vacías tiene cada documento,                             **
    - Que elimine los símbolos de puntuación y                                **
    - Que muestre todas las palabras que contiene cada documento de manera ordenada,    **
    - Que muestre cuantas palabras (longitud) contiene cada documento                   **

    - Que una los dos documentos en otro documento .txt con otro nombre y que elimine los símbolos                          **
    - De puntuación y que muestre todas las palabras que contiene el documento nuevo    **
    - De manera ordenada y            **
    - Que muestre cuantas palabras (longitud) contiene el documento                     **
    - Que escriba una palabra y la busque e indique si la encontró o no                 **
"""

"""
Por defecto, el modo de abrir un fichero es lectura como texto. Por tanto, para leer su contenido no es necesario especificar el segundo argumento, es decir:
    fichero = open('./file.txt', 'rt') = fichero = open('./file.txt')
    x -> read
    w -> write
    a -> append
    x -> create
    t -> text-mode
    b -> bytes - para archivos como fotos
"""


import os
input_files_path = "./input_files"
output_files_path = "./output_files/Union.txt"

files_names = os.listdir(input_files_path)

"""
Leé cada documento que hay dentro de la carpeta de entrada; posterior a ello, leé las líneas con texto y las líneas vacias, y el total de cada una, las imprime.
"""

for file_name in files_names:
    file_path = input_files_path + "/" + file_name
    numLineas = 0
    numLineasVacias = 0
    with open(file_path, 'rt', encoding='utf-8') as fichero:
        listaDeLineas = fichero.readlines()
    for linea in listaDeLineas:
        if linea.strip() == "":
            numLineas += 1
            numLineasVacias += 1
        else:
            numLineas += 1
    fichero.close()
    print(f"Información del fichero '{file_name}'")
    print(f"Lineas con texto: {numLineas}")
    print(f"Lineas vacías: {numLineasVacias} \n")
    print("---------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------
"""
Leé cada documento que hay dentro de la carpeta de entrada; y elimina los símbolos de todo el texto en base a los símbolos que 
hay agregados al vector después, imprime alfabéticamente cada palabra de cada documento de texto e imprime la cantidad de palabras en él.
"""

simbolos = ['(', ')', ',', '.', ';', ':', '/', '"']

for file_name in files_names:
    file_path = input_files_path + "/" + file_name
    with open(file_path, 'rt', encoding='utf-8') as fichero:
        texto = fichero.read()
    for simbolo in simbolos:
        texto = texto.replace(simbolo, " " + simbolo + " ")
    palabras_lista = texto.split()
    palabras_lista.sort()
    print(f"Orden alfabetico de las palabras en el fichero '{file_name}'")
    for palabra in palabras_lista:
        print(palabra)
    print(
        f"Cantidad de palabras en el fichero '{file_name}': {len(palabras_lista)} \n")
    fichero.close()
    print("---------------------------------------------------------------------------------")


# ---------------------------------------------------------------------------------
"""
Leé cada archivo dentro de la carpeta de entrada y toma todo el texto de cada uno para ponerlo dentro del archivo que hay en la carpeta de salida.
"""

union = ""
for file in files_names:
    archivo = open(input_files_path + "/" + file_name)
    texto = archivo.read()
    archivo.close()
    union += texto

with open(output_files_path, 'wt') as salida:
    salida.write(union)
archivo.close()
print("---------------------------------------------------------------------------------")


# ---------------------------------------------------------------------------------
"""
Leé el documento que hay en la carpeta de salida y elimina los símbolos de todo el documento en base a los símbolos que hay agregados al vector definido 'simbolos';
posterior a ello, imprime alfabéticamente cada palabra del documento de texto e imprime la cantidad de palabras que hay en él.
"""

with open(output_files_path, 'rt', encoding='utf-8') as fichero:
    texto = fichero.read()
for simbolo in simbolos:
    texto = texto.replace(simbolo, " " + simbolo + " ")
palabras_lista = texto.split()
palabras_lista.sort()
print(f"Orden alfabetico de las palabras en el fichero 'Union.txt'")
for palabra in palabras_lista:
    print(palabra)
print(
    f"Cantidad de palabras en el fichero 'Union.txt': {len(palabras_lista)} \n")
fichero.close()
print("---------------------------------------------------------------------------------")


# ---------------------------------------------------------------------------------
"""
Se le solicita al usuario que ingrese una palabra (la cuál se valida que sea de tipo string o cadena), y si dicha palabra existe o no en el documento se imprime un mensaje,
dependiendo el caso. Sin embargo, si el usuario ingresa un dato diferente de string o cadena se imprimirá un mensaje de error.
"""

while True:
    search_word = input("\nIngresa una palabra: ")
    if search_word.isalpha():
        with open(output_files_path, 'rt', encoding='utf-8') as fichero:
            listaDeLineas = fichero.read()

        if search_word in listaDeLineas:
            print(f"La palabra '{search_word}' existe dentro del documento")
        else:
            print(f"La palabra '{search_word}' no existe dentro del documento")
        break
    else:
        print("Error. Por favor, ingrese una palabra")
        continue
print("---------------------------------------------------------------------------------")

