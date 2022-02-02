#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

vogal = ['a','e','i','o','u']

letra = input('')

if letra == vogal[0] or letra == vogal[1] or letra == vogal[2] or letra == vogal[3] or letra == vogal[4]:
    print('Vogal')
else:
    print('Consoante')