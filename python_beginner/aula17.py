"""
Aula 17 - Condicionais (if / else / elif) entendendo o fluxo do interpretador
"""
# if / elif / else
# se / se nao se  / se nao
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('condição 1')
elif condicao2:
    print('condição 2')
elif condicao3:
    print('condição 3')
elif condicao4:
    print('condição 4')
else:
    print('Nenhuma condição valida!')

if 10 == 10:
    print('Outro if')

print('Fora do if')