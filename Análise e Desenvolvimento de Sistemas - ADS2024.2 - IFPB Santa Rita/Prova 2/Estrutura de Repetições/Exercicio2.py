#Joseph Nichollas Abreu Cavalcante

# 2. Crie um programa que receba um número inteiro do usuário e imprima a tabuada desse número (do 1 ao 10). 
# Use uma estrutura de repetição para calcular e exibir cada linha da tabuada.

numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"\nTabuada do {numero}:")

for i in range(1, 11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")