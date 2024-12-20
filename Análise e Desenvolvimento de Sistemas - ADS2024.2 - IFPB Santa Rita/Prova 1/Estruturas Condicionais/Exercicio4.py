#Joseph Nichollas Abreu Cavalcante

# 4. Escreva um programa que peça ao usuário para digitar uma letra e verifique se ela é uma vogal ou uma consoante.

letra= input('digite uma letra (minúscula):')
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u' :
    print('Essa letra é vogal')
else:
    print('Essa letra é consoante')