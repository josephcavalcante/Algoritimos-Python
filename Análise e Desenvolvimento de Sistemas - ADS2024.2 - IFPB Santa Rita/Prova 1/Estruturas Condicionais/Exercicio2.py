#Joseph Nichollas Abreu Cavalcante 

# 2. Escreva um programa que receba três notas de 0 a 10, 
# calcule a média e informe se o aluno foi aprovado (média >= 7), reprovado (média < 4) ou está em recuperação (7 > média >=4).

nota1 = float(input('digite sua primeira nota(0 a 10):'))
nota2 = float(input('digite sua segunda nota(0 a 10):'))
nota3 = float(input('digite sua terceira nota(0 a 10):'))
media= ((nota1 + nota2 + nota3)/3)
if  media >= 7 :
    print('você está aprovado, esta é sua média:', media)
elif  media >= 4 :
    print('você está em recuperação, esta é sua média:', media)
else:
    print('você está reprovado, esta é sua média:', media)