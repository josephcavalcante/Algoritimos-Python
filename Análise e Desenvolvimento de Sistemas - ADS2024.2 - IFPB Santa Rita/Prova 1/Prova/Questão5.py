# Joseph Nichollas Abreu Cavalcante

# 5. Escreva um programa que solicite ao usuário três números inteiros e informe qual deles é o maior.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = int(input("Digite o terceiro número inteiro: "))
maior = num1 

if num2 > maior:
    maior = num2  
if num3 > maior:
    maior = num3  

print(f"\nO maior número é: {maior}")