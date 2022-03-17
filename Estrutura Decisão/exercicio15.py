'''
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os
valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é:
equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

lado_01, lado_02, lado_03 = map(float,input().split())

if lado_01 == lado_02 and lado_01 == lado_03:
    print('Triângulo Equilátero')
elif lado_01 == lado_02 or lado_01 == lado_03:
    print('Triângulo Isósceles')
else:
    print('Triângulo Escaleno')
