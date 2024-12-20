#Joseph Nichollas Abreu Cavalcante

# 3. Faça um programa em python que receba um inteiro e calcule seu valor fatorial.

numero=int(input('digite um número para descobrir o fatorial: '))
fatorial=1

for i in range(1, numero +1):
    fatorial*=i

print(f'O Fatorial do número é {fatorial}')