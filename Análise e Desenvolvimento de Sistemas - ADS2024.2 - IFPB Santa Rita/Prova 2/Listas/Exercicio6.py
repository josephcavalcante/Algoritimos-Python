#Joseph Nichollas Abreu Cavalcante

# 6. Escreva um programa que receba uma lista de 10 números inteiros do usuário. 
# Em seguida: Calcule a média dos números.
# Exiba os números maiores que a média.

lista=[]
for i in range(10):
   num=int(input('digite um numero inteiro:'))
   lista.append(num)
media=(sum(lista)/10)
print(media)
lista_m=[]
for i in lista:
    if i>=media:
        lista_m.append(i)
print(lista_m)