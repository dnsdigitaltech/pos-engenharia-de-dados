import re

texto = "No dia 07/07/1822, foi proclamada a independência do Brasil e no dia 15/11/1899, foi proclamada a república no Brasil"

# Padrão: dia/mês/ano
padrao = r'\b(\d{1,2})/(\d{1,2})/(\d{4})\b'

combinacoes = re.findall(padrao, texto)

datas = []

for d in combinacoes:
    dia = int(d[0])
    mes = int(d[1])
    ano = int(d[2])

    datas.append((dia, mes, ano))

print(datas)