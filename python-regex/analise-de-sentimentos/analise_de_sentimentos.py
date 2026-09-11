import re

#Listas de palavras positivas e negativas
palavras_positivas = ['bom', 'excelente', 'feliz']
palavras_negativas = ['ruim', 'péssimo', 'triste']

texto = "O filme foi excelente. De fato, foi muito bom."

#Contar a quantidade de palavras positivas e negativas que a regex vai procurar no texto
qtd_positiva = len(re.findall(r'\b(?:%s)\b' % '|'.join(palavras_positivas), texto, flags=re.IGNORECASE))
qtd_negativa = len(re.findall(r'\b(?:%s)\b' % '|'.join(palavras_negativas), texto, flags=re.IGNORECASE))

#Comparar qual a quantidade predominante entre os termos positivos e negativos.
sentimento='Neutro'
if qtd_positiva > qtd_negativa:
  sentimento='Positivo'
elif qtd_negativa > qtd_positiva:
   sentimento='Negativo'


print(f'O sentimento sobre o filme foi: {sentimento}')