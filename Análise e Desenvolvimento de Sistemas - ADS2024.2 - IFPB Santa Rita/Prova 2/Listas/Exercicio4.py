#Joseph Nichollas Abreu Cavalcante

# 4. Peça ao usuário para inserir uma lista de  10 números inteiros. Em seguida:
# Conte e exiba quantas vezes os números pares aparecem na lista.
# Exiba os números ímpares e suas respectivas posições na lista.

lista=[]
listapar=[]
listaimpar=[]
for i in range(10):
   num=int(input('digite um numero inteiro:'))
   lista.append(num)   
for i in lista:
    if i%2==0:
        listapar.append(i)
    else:
        listaimpar.append(i)
        listaimpar.append(lista.index(i))
print(len(listapar))
print(listaimpar)
        
