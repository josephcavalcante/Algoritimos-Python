#Joseph Nichollas Abreu Cavalcante

# 6. Crie um programa que solicite ao usuário um número inteiro positivo e determine se ele é um número primo. 
# Para isso, utilize uma estrutura de repetição para verificar quantos divisores o número possui.

numero = int(input("Digite um número inteiro positivo: "))

if numero > 1:
    divisores = 0
    
    for i in range(1, numero + 1):
        if numero % i == 0:  
            divisores += 1
    if divisores == 2:
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")
else:
    print("Por favor, digite um número inteiro positivo maior que 1.")