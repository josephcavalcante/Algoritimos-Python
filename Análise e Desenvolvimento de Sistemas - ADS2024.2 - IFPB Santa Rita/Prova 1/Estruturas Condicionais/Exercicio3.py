#Joseph Nichollas Abreu Cavalcante 

# 3. Escreva um programa que receba o salário de um funcionário e calcule o valor com o aumento, de acordo com a seguinte regra:
# Salário até R$ 1.000,00: aumento de 20%
# Salário entre R$ 1.000,01 e R$ 2.000,00: aumento de 15%
# Salário acima de R$ 2.000,00: aumento de 10%

salario = float(input('digite o valor do seu salário:'))
if salario <= 1000 :
    print('seu salário com aumento fica:', salario * 1.20 )
elif salario <= 2000 :
    print('seu salário com aumento fica:', salario * 1.15)
else:
    print('seu salário com aumento fica:', salario * 1.10)