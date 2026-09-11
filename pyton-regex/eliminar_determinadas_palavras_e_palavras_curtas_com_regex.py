import re

texto = "Este texto é um exemplo para fazer um checklist de revisão do motor do carro."

palavras_para_eliminar = ["este", "para", "de"]

texto = texto.lower()

# Cria o padrão das palavras específicas
palavras = "|".join(map(re.escape, palavras_para_eliminar))

# Remove as palavras específicas OU palavras com 1 ou 2 caracteres
padrao = rf'\b({palavras})\b|\b\w{{1,2}}\b'

texto = re.sub(padrao, '', texto)

# Remove espaços duplicados
texto = re.sub(r'\s+', ' ', texto).strip()

print(f'O resultado é: {texto}')