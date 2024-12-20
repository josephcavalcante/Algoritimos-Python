#Joseph Nichollas Abreu Cavalcante

# 4. Escreva um programa que peça ao usuário para digitar um número inteiro positivo.
# Caso o usuário digite um valor inválido (número negativo ou zero), 
# o programa deve continuar solicitando até que um valor válido seja informado. 

while True:
    numero = int(input("Digite um número inteiro positivo: "))
    if numero > 0:
        print(f"\nNúmero válido informado: {numero}")
        break
    else:
        print("Valor inválido! Por favor, digite um número inteiro positivo.")