"""Escribe el texto cuyo pos_tag quieres contar.
Algunas palabras están en mayúsculas y otras en minúsculas, por lo que conviene transformar todas las palabras en minúsculas antes de aplicar la tokenización.
Pase las palabras a través de word_tokenize desde nltk.
Calcular el pos_tag de cada token"""
from cgitb import text
from collections import Counter
import nltk
text = " Guru99 is one of the best sites to learn WEB, SAP, Ethical Hacking and much more online."
lower_case = text.lower()
tokens = nltk.word_tokenize(lower_case)
tags = nltk.pos_tag(tokens)
counts = Counter(tag for word, tag in tags)
print(counts)