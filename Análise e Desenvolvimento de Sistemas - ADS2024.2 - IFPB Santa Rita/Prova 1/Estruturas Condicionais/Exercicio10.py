#Joseph Nichollas Abreu Cavalcante

# 10. Escreva um programa em Python que receba o peso (em kg) e a altura (em metros) de uma pessoa, 
# calcule o Índice de Massa Corporal (IMC) e exiba uma mensagem indicando a categoria de acordo com o resultado.
# A fórmula para calcular o IMC é:
# imc = peso / altura ** 2
# Use as seguintes classificações para o IMC:

# Abaixo do Peso: IMC < 18.5
# Peso Normal: IMC entre 18.5 e 24.9
# Sobrepeso: IMC entre 25 e 29.9
# Obesidade Grau I: IMC entre 30 e 34.9
# Obesidade Grau II: IMC entre 35 e 39.9
# Obesidade Grau III (Obesidade Mórbida): IMC ≥ 40

peso = float(input("digite seu peso (kg): "))
altura = float(input("digite sua altura (metros): "))
imc = peso / altura ** 2
if imc < 18.5:
    print("categoria: abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("categoria: peso normal")
elif 25 <= imc < 29.9:
    print("categoria: sobrepeso")
elif 30 <= imc < 34.9:
    print("categoria: obesidade grau I")
elif 35 <= imc < 39.9:
    print("categoria: obesidade grau II")
else:
    print("categoria: obesidade grau III (obesidade mórbida)")