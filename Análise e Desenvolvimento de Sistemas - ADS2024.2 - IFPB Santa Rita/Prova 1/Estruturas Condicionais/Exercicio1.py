#Joseph Nichollas Abreu Cavalcante

# 1. Escreva um programa que receba a idade de uma pessoa e determine se ela é menor de idade (menor que 18 anos), adulta (entre 18 e 60 anos) ou idosa (maior que 60 anos)

idade = int(input('digite sua idade:'))
if idade < 18 :
    print('você é menor de idade')
elif idade > 60 :
    print('você é idoso')
else:
    print('você é adulto') 