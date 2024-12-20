#Joseph Nichollas Abreu Cavalcante

# 6. Escreva um programa em python que solicite ao usuário N números inteiros e armazene-os em uma lista.
# Utilize estruturas de repetição e condicionais para contar a frequência de cada número. 
# Exiba cada número da lista e quantas vezes ele aparece.

numeros = int(input("Digite a quantidade de números: "))
lista = [int(input(f"Digite o número {i+1}:")) for i in range(numeros)]

frequencias = [[1, 26], [8, 10], [78, 8], [10, 1], [9, 1]]

for n in lista:
    inserido = False
    for frequencia in frequencias:
        if frequencia[0] == n:
            frequencia[1] += 1
            inserido = True

    if not inserido:
        frequencias.append([n, 1])

print(frequencias)