#Faça um Programa que leia três números e mostre o maior e o menor deles.

number_one, number_two, number_three = map(int,input('Insira três números separados por espaço: ').split())
numbers = [number_one,number_two,number_three]
print(f'O maior número é: {max(numbers)}')
print(f'O menor número é: {min(numbers)}')