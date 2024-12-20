#Joseph Nichollas Abreu Cavalcante

# 2. Faça um programa que receba primeiramente a quantidade de idades que serão fornecidas. 
# Em seguida, receba a quantidade de idades informada e imprima: 
# quantos são menores de idade (idade < 18); 
# quantos são adultos (idade entre 18 e 60); 
# quantos são idosos (idade >= 60).

quantidade=int(input('digite a quantidade de idades a serem avaliadas:'))
menor_idade=0
adulto=0
idoso=0

for i in range(1, quantidade +1):
    idade=int(input('digite a idade:'))
    if idade <=18:
        menor_idade+=1
    elif 18<=idade<60:
        adulto+=1
    else:
        idoso+=1 

print(f"Menores de idade: {menor_idade}")
print(f"Adultos: {adulto}")
print(f"Idosos: {idoso}")