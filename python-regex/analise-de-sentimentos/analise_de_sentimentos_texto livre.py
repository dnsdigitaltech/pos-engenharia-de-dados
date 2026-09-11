import re

palavras_positivas = ['bom', 'excelente', 'feliz']
palavras_negativas = ['ruim', 'péssimo', 'triste']

texto = "O filme foi excelente. De fato, foi muito bom, mas teve um final triste."

# Contar palavras positivas
qtd_positiva = len(
    re.findall(
        r'\b(?:%s)\b' % '|'.join(palavras_positivas),
        texto,
        flags=re.IGNORECASE
    )
)

# Contar palavras negativas
qtd_negativa = len(
    re.findall(
        r'\b(?:%s)\b' % '|'.join(palavras_negativas),
        texto,
        flags=re.IGNORECASE
    )
)

# Definir o sentimento
sentimento = 'Neutro'

if qtd_positiva >= 2 * qtd_negativa:
    sentimento = 'Positivo'

elif qtd_negativa >= 3 * qtd_positiva:
    sentimento = 'Negativo'

print(f'Palavras positivas: {qtd_positiva}')
print(f'Palavras negativas: {qtd_negativa}')
print(f'O sentimento do texto foi: {sentimento}')