#Joseph Nichollas Abreu Cavalcante

#8. Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

n1 = float(input('digite o primeiro número:'))
n2 = float(input('digite o segundo número:'))
n3 = float(input('digite o terceiro número:'))
maior = n1
menor = n1
if n2 > maior:
   maior = n2
elif n3 > maior:
    maior = n3

if n2 < menor:
    menor = n2
elif n3 < menor:
    menor = n3
print('maior:', maior)
print ('menor:', menor)