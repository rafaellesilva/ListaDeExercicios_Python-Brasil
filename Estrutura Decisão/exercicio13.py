'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

number_week = int(input('Enter value of the number of week: '))
if number_week == 1:
    print('Sunday')
elif number_week == 2:
    print('Monday')
elif number_week == 3:
    print('Tuesday')
elif number_week == 4:
    print('Wednesday')
elif number_week == 5:
    print('Thursday')
elif number_week == 6:
    print('Friday')
elif number_week == 7:
    print('Saturday')
else:
    print('Invalid value')