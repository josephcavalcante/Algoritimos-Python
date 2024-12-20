# Joseph Nichollas Abreu Cavalcante

# 4. Escreva um programa em Python que pergunte ao usuário a sua idade. O programa deve verificar se a idade está entre 18 e 75 anos. 
# Caso esteja, exiba a mensagem "Idade dentro da faixa permitida para trabalho". Caso contrário, exiba "Idade fora da faixa permitida".

idade = int(input("Digite a sua idade: "))

if 18 <= idade <= 75:
    print("Idade dentro da faixa permitida para trabalho.")
else:
    print("Idade fora da faixa permitida.")