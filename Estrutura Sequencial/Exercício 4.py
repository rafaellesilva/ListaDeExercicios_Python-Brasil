# Faça um Programa que peça as 4 notas bimestrais e mostre a média
nota_1,nota_2,nota_3,nota_4 = map(float,input('Informe as 4 notas bimestrais:').split())
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(f'A média do aluno é: {round(media)}')
