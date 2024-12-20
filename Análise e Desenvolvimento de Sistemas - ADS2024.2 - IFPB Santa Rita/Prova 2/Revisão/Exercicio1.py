#Joseph Nichollas Abreu Cavalcante

# 1. Faça um programa em python que solicite números ao usuário enquanto ele não digita o valor X, ao digitar o valor X, 
# o programa irá calcular a média dos números digitados e imprimir na tela.

lista=[]
while True:
    numero=float(input('digite um número:'))
    lista.append(numero)
    if numero == 10:
        break
print (f"A média dos números digitados é: {sum(lista)/len(lista)}")