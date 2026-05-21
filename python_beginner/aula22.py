"""
Aula 22 - Operador logico "or"

Operadores logicos
and (e) or (ou) not (nao)
OR - qualquer condicao verdadeira avalia toda expresao como verdadeira
a expressao inteira será avaliada naquele valor
sao considerados falsy
0 0.0 '' False
tambem existe o tipo None que é usado para representar um não valor
"""
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avalicao de curtto circuito
senha = input('Senha: ') or 'Sem Senha'
print(senha)
print(0 or False or 0 or 'abc' or True)