import nltk
#nltk.download('punkt')

input_file_path = "./Archivo.txt"

with open(input_file_path, 'rt', encoding='utf-8') as archivo:
    texto = archivo.read()

tokens = nltk.word_tokenize(texto, "spanish")
for token in tokens:
    print(token)

palabras_total = len(tokens)
print(f"Palabras {palabras_total}")

tokens_conjunto = set(tokens)
palabras_diferentes = len(tokens_conjunto)
print(f"Palabras diferentes: {palabras_diferentes}")

riqueza_lexica = palabras_diferentes / palabras_total
riqueza_lexicap = 100 * palabras_diferentes / palabras_total
print(f"Riqueza lexia: {riqueza_lexica} = {int(riqueza_lexicap)}%")
print("==============================")
texto_nltk = nltk.Text(tokens)
palabra = input("Ingresa una palabra: ")
texto_nltk.concordance(palabra)
print("==============================")
texto_nltk.similar(palabra)
print("==============================")
conteo_individual = tokens.count(palabra)
print(f"Cantidad de veces que se repite '{palabra}': {conteo_individual}")