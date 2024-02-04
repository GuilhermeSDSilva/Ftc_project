import re


def extrair_valor(chave, texto):
    padrao = rf"'{chave}': (\d+)"
    correspondencia = re.search(padrao, texto)
    return correspondencia.group(1) if correspondencia else None

texto = """{ ’inicial’: 0, ’aceita’: 1, ’rejeita’: 2,
delta: [ (0,0,0,1,D),(0,0,1,0,D),(0,3,b,b,E),
˙(3,1,0,0,P),(3,1,1,1,P)] }
3
100
10101
000000000"""

padrao_delta = r'delta: \[([^]]+)\]'
match_delta = re.search(padrao_delta, texto)


# Exemplos de uso
inicial = extrair_valor("inicial", texto)
aceita = extrair_valor("aceita", texto)
rejeita = extrair_valor("rejeita", texto)


# Substitui tudo entre chaves por uma string vazia
padrao_chaves = r'\{[^}]*\}'
texto_sem_chaves = re.sub(padrao_chaves, '', texto)
print(texto_sem_chaves.strip())


if match_delta:
    delta_str = match_delta.group(1)
    delta = re.findall(r'\(([^)]+)\)', delta_str)
    
    
else:
    print("Padrão não encontrado.")
    
 