#Joseph Nichollas Abreu Cavalcante

# 5. Escreva um programa que receba três valores numéricos e verifique se eles podem formar os lados de um triângulo.
# Critério: Para que três valores formem um triângulo, a soma de quaisquer dois lados deve ser maior que o terceiro.

lado1 = float(input('digite o valor do primeiro lado:'))
lado2 = float(input('digite o valor do segundo lado:'))
lado3 = float(input('digite o valor do terceiro lado:'))
if (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado3 + lado1 > lado2) :
    print('um triângulo pode ser formado')
else:
    print('um triângulo não pode ser formado')
