#Joseph Nichollas Abreu Cavalcante

# 3. Implemente um programa em Python que crie uma lista com 10 números inteiros aleatórios entre 1 e 100. 
# Em seguida, use um loop para calcular e 
# exibir a soma de todos os elementos que estão em índices pares na lista.

import random
lista=[]
lista_i=[]
for x in range(10):
    x= random.randint(1,100)
    lista.append(x)
for i in range(len(lista)):
    if lista[i]%2==0:
        lista_i.append(i)
        
print(sum(lista_i))


