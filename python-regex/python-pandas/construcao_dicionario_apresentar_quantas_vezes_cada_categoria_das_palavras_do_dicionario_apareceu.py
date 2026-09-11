import pandas as pd
import re

dicionario = {
    'fruta': ['maçã', 'banana', 'laranja'],
    'animal': ['cachorro', 'leão', 'peixe'],
    'veiculo': ['carro', 'moto', 'onibus']
}

texto = "meu cachorro gosta de passear de carro e de comer maçã."

# Remover pontuação
padrao_sem_pontuacao = r'[^\w\s]'
texto = re.sub(padrao_sem_pontuacao, '', texto)

# Converter para minúsculas
texto = texto.lower()

# Criar DataFrame
df = pd.DataFrame(dicionario)

# Dicionário para armazenar a quantidade de cada categoria
quantidade = {
    'fruta': 0,
    'animal': 0,
    'veiculo': 0
}

# Percorrer as categorias
for categoria, palavras in dicionario.items():

    # Percorrer as palavras de cada categoria
    for palavra in palavras:

        # Procurar a palavra no texto
        encontrados = re.findall(r'\b' + re.escape(palavra) + r'\b', texto)

        # Somar a quantidade encontrada
        quantidade[categoria] += len(encontrados)

# Mostrar resultado
print("Quantidade por categoria:")

for categoria_total, qtd in quantidade.items():
    print(f"{categoria_total}: {qtd}")