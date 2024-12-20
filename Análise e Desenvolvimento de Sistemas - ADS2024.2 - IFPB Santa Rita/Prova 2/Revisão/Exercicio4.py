#Joseph Nichollas Abreu Cavalcante

# 4. Escreva um programa em python que leia um número inteiro N e gere uma lista com os números de 1 até N. 
# Para cada número na lista substitua por "Fizz" se for múltiplo de 3;
# substitua por "Buzz" se for múltiplo de 5; 
# substitua por "FizzBuzz" se for múltiplo de 3 e 5; 
# exiba a lista modificada.

# Ex. Digite o valor de N: 15  

# Lista resultante:  
# [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

numero=int(input('Digite o número: '))
lista=[]
for i in range(1, numero+1):
    if i%3==0 and i%5==0:
        lista.append('FizzBuzz')
    elif i%5==0:
        lista.append('Buzz')
    elif i%3==0:
        lista.append('Fizz')
    else:
        lista.append(i)
print(lista)