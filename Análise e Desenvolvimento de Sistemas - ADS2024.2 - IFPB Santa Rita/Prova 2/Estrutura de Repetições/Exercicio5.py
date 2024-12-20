#Joseph Nichollas Abreu Cavalcante

# 5. Crie um programa em Python que solicite ao usuário um número inteiro positivo N. 
# O programa deve gerar e exibir a série de Fibonacci contendo N números.
# Exemplo: Se o usuário informar N=6, o programa deverá exibir:
# 0, 1, 1, 2, 3, 5

n = int(input("Digite um número inteiro positivo N para gerar a série de Fibonacci: "))

if n > 0:
    penultimo = 0
    ultimo = 1
    for i in range(n):
        print(penultimo)
        resultado = ultimo
        penultimo = ultimo
        ultimo = resultado + penultimo
else:
    print("Por favor, digite um número inteiro positivo.")