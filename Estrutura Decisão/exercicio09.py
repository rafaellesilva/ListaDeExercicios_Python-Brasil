#Faça um Programa que leia três números e mostre-os em ordem decrescente.
number_one,number_two,number_three = map(int,input('Insira três valores separados por espaço: ').split())
numbers_list = [number_one,number_two,number_three]
numbers_list.sort(reverse=True)
print(numbers_list)

