import pandas as pd

#Dicionário de palavras
dicionario = {'fruta': ['maçã', 'banana', 'laranja'],
              'animal': ['cachorro', 'leão', 'peixe'],
              'veiculo': ['carro', 'moto', 'onibus']}


df = pd.DataFrame(dicionario)

#Lista com o Dataframe
palavras_dicionario = df.to_dict('list')

#Contar a quantidade de vezes que cada item aparece
qtd_item = {}
for key, values in palavras_dicionario.items():
    for valor in values:
        qtd_item[valor] = qtd_item.get(valor, 0) + 1

#Exibir o item e a quantidade de vezes que ele aparece
print("Quantidade de Itens:")
for item, qtd in qtd_item.items():
    print(f"{item}: {qtd}")