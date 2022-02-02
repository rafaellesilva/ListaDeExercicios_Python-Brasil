'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

value_one,value_two,value_three = map(int,input('Insira três números separados por espaço: ').split())
print(f'O produto que você deve comprar, é o que custa R$ {min(value_one,value_two,value_three)}, sendo o mais em conta.')