import re

texto = "Este é um texto simples que deve ser testado."

#Encontrar palavras >=4
tokens = re.findall(r'\w{4,}', texto)

print(tokens)