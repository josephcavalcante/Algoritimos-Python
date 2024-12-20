#Joseph Nichollas Abreu Cavalcante
# 2. Escreva um programa em Python que solicite ao usuário um número inteiro positivo N.
# O programa deve calcular e exibir a soma dos N primeiros números da série de Fibonacci.
# Exemplo: Se o usuário informar N=5, o programa deve exibir:
# Soma dos primeiros 5 números da série de Fibonacci: 7

while True:
    n1=int(input('digite um número inteiro e positivo: '))
    if n1 <= 0:
        print('digite um numero positivo!')
        continue
    else:
        penultimo= 0
        ultimo = 1
        resultado=0
        for i in range (n1):
            resultado+= penultimo
            prox= penultimo + ultimo
            penultimo = ultimo
            ultimo = prox
        print(f"Soma dos primeiros {n1} números da série de Fibonacci: {resultado}")