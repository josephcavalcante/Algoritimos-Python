#Joseph Nichollas Abreu Cavalcante 

# 6. Escreva um programa que receba o nome de um produto e sua categoria ("alimento", "limpeza" ou "bebida") e aplique um desconto com base na categoria:
# Alimento (valor 100.50): 10%
# Limpeza (valor 34.20): 20%
# Bebida (valor 7.80): 5%
# Mostre o valor final com o desconto aplicado.

produto = input('digite o nome do produto:')
categoria = input('digite a categoria (alimento, limpeza ou bebida):')
if categoria == "alimento" or categoria == "Alimento" :
    print('valor com desconto aplicado:', 100.50 * 0.90)
elif categoria == "limpeza" or categoria == "Limpeza" :
    print('valor com desconto aplicado:', 34.20 * 0.80)
elif categoria == "bebida" or categoria == "Bebida" :
    print('valor com desconto aplicado:', 7.80 * 0.95)