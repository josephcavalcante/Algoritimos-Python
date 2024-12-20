#Joseph Nichollas Abreu Cavalcante

# 4. Crie um programa que solicite dois números inteiros positivos A e B, com A≥B. 
# O programa deve calcular o quociente da divisão de A por B utilizando apenas subtrações e uma estrutura de repetição. 
# O programa deve exibir o quociente e o resto da divisão.
# Exemplo: Se o usuário informar A=13 e B=4, o programa deve exibir: Quociente: 3 Resto: 1

while True:
    n1=int(input('digite um número inteiro e positivo: '))
    n2=int(input('digite outro número inteiro e positivo: '))
    if n1 <= 0 or n2 <= 0:
        print('digite números positivos!')
        continue
    elif n1<n2:
        print('digite o primeiro número maior que o segundo')
        continue
        
    else:
        quo=0
        resto=n1
        while resto >= n2:
            resto-= n2
            quo += 1
    print(f"Quociente: {quo} Resto: {resto}")