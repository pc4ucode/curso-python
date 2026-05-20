"""
Aula 16 - Condicionais (if / else / elif)
"""
# if / elif / else
# se / se nao se  / se nao
entrada = input('Você quer "entrar" ou "sair"?')

if entrada == 'entrar':
    print('Você entrou no sistema!')
elif entrada == 'sair':
    print('Você saiu do sistema!')
else:
    print('Opção inválida!Você não digitou nem entrar e nem sair!')

print('Fora dos blocos de condição!')