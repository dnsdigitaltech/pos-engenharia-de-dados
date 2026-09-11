import re

#Texto que vamos manipular e das palavras que queremos eliminar
texto = "Este texto é um exemplo para fazer um checklist de revisão do motor do carro."
palavras_para_eliminar = ["este", "para", "de"]
texto = texto.lower()

#Verificamos cada uma das palavras que devem ser eliminadas
for palavra in palavras_para_eliminar:
  padrao = r'\b%s\b' % re.escape(palavra)
  texto = re.sub(padrao, '', texto)

print(f'O resultado é: {texto}')