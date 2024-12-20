# Joseph Nichollas Abreu Cavalcante

# 6. Faça um programa em que o usuário informe o salário recebido e o total gasto com despesas. 
# Deverá ser exibido  na  tela  "Gastos  dentro  do  orçamento"  
# caso  o  valor  gasto  não  ultrapasse  o  valor  do  salário  
# e "Orçamento estourado" se o valor gasto ultrapassar o valor do salário.

salario = float(input("Digite o salário recebido: R$ "))
despesas = float(input("Digite o total gasto com despesas: R$ "))

if despesas <= salario:
    print("\nGastos dentro do orçamento.")
else:
    print("\nOrçamento estourado.")