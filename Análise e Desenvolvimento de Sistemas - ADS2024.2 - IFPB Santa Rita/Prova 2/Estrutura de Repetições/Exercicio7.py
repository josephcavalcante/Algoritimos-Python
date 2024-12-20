#Joseph Nichollas Abreu Cavalcante

# 1. Faça um programa que peça ao usuário um número inteiro positivo e exiba esse número ao contrário. 
# Por exemplo, se o usuário digitar 12345, o programa deve exibir 54321. 
# Utilize uma estrutura de repetição para calcular o número reverso.

while True:
    n1=int(input('digite um número inteiro: '))
    if n1 <= 0:
        print('digite um numero positivo!')
        continue
    else:
        n2= ""
        while n1 > 0:
            ultimo= n1 % 10
            n2 += str(ultimo)
            n1 //= 10
        print(int(n2))           