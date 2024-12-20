#Joseph Nichollas Abreu Cavalcante

# 9. Faça um Programa que leia um número e exiba o dia correspondente da semana. 
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

num = int(input('digite um número(1 a 7):'))
if num == 1:
    print('domingo')
elif num == 2:
    print('segunda')
elif num == 3:
    print('terça')
elif num == 4:
    print('quarta')
elif num == 5:
    print('quinta')
elif num == 6:
    print('sexta')
elif num == 7:
    print('sábado')
else:
    print('valor inválido')