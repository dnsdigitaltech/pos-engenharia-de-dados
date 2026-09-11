import re

texto = "Existem várias datas comemorativas, como o natal no dia 25/12 e 1/1"

padrao = r'\b(\d{1,2})/(\d{1,2})\b'

combinacoes = re.findall(padrao, texto)

datas = []
for d in combinacoes:
  dia = int(d[0])
  mes = int(d[1])  
  datas.append((dia, mes))

print(datas)