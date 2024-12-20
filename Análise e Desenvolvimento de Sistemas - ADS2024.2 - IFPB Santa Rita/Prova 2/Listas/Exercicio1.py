#Joseph Nichollas Abreu Cavalcante

# 1. Escreva um programa em Python que receba 5 números inteiros do usuário e os armazene em uma lista. 
# Após isso, use um loop para calcular e exibir:
# A soma de todos os números.
# O maior número da lista.
# O menor número da lista.

lista=[]
for i in range(5):
   num=int(input('digite um numero:'))
   lista.append(num)
print(sum(lista))
print(max(lista))
print(min(lista))