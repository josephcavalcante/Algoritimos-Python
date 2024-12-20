#Joseph Nichollas Abreu Cavalcante

# 5. Escreva um programa que solicite N números inteiros e armazene-os em uma lista. 
# Utilize estruturas condicionais para criar uma nova lista contendo apenas os números positivos.
# Calcule e exiba a média dos números positivos. 
# Caso não existam números positivos, exiba uma mensagem apropriada. 

lista=[]
for numero in range(10):
    numero=int(input('digite um número inteiro: '))
    lista.append(numero)
positivos=[i for i in lista if i > 0]

if  not positivos:
    print('Não há nenhum número positivo na lista :(')

else:
    print(f'Aqui está a média dos números positivos:{sum(positivos)/len(positivos)}')