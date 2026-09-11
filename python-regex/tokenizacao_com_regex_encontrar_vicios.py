import re

texto = "Este é um texto, né? Temos que encontrar os vícios de linguagem, enfim."

resultado = re.search(r"\b(né|enfim)\b", texto, re.IGNORECASE)

if resultado:
    print("Encontrou:", resultado.group())
else:
    print("Nenhum vício encontrado.")