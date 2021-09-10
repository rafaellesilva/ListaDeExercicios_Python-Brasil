#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho = float(input('Usuário, informe o tamanho da área a ser pintada em m²: '))

quantidade_litros = tamanho / 3
quantidade_latas = quantidade_litros / 18
if quantidade_latas > 1:
    quantidade_latas = quantidade_latas
else:
    quantidade_latas = 1
preço = 80 * quantidade_latas

print(f'Usuário, a quantidade de latas necessárias para pintar {tamanho:.0f} m² é: {quantidade_latas} lata(s)\nPreço total: R$ {preço:.2f}')

