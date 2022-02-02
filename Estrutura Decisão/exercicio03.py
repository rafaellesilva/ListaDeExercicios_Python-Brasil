'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = input('Insira o sexo: ')
if sexo.upper() == 'F':
    resposta = 'Feminino'
elif sexo.upper() == 'M':
    resposta = 'Masculino'
else:
    resposta = 'Sexo inválido'

print(resposta)