#Joseph Nichollas Abreu Cavalcante

# 3. Escreva um programa que peça ao usuário dois números inteiros positivos A e B. 
# O programa deve calcular o produto de A e B utilizando apenas adição e uma estrutura de repetição.
# Exemplo: Se o usuário informar A=4 e B=3,
# o programa deve exibir: 4 x 3 = 12

while True:
    n1=int(input('digite um número inteiro e positivo: '))
    n2=int(input('digite outro número inteiro e positivo: '))
    if n1 <= 0 or n2 <= 0:
        print('digite números positivos!')
        continue
    else:
        mult=0
        for i in range(n2):
            mult+=n1
        print(f"{n1} x {n2} = {mult}")