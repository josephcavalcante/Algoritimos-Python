#Joseph Nichollas Abreu Cavalcante

# 1. Escreva um programa que peça ao usuário um número inteiro positivo N
# e calcule a soma dos números de 1 a N utilizando uma estrutura de repetição.

n = int(input("Digite um número inteiro positivo: "))
if n > 0:
    soma = 0 
    for i in range(1, n + 1):
        soma += i 
    print(f"\nA soma dos números de 1 a {n} é: {soma}")
else:
    print("\nPor favor, digite um número inteiro positivo.")