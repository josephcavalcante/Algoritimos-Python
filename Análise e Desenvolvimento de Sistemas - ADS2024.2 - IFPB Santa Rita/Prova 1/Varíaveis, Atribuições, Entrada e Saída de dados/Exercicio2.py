# #Joseph Nichollas Abreu Cavalcante

# #2. Crie um programa que solicite ao usuário o seguinte:
# Nome (string)
# Idade (inteiro)
# Altura (float)
# É estudante? (booleano, onde o usuário deve digitar "Sim" ou "Não")
# Exiba uma mensagem com os dados inseridos, por exemplo:
# Nome: Maria, Idade: 25 anos, Altura: 1.65m, Estudante: True

nome=input('digite seu nome:')
idade= int(input('digite sua idade:'))
altura= float(input('digite sua altura:'))
estudante=bool(input('você é estudante? Digite sim ou não:'))
print ('Seus dados:')
print ('Nome:', nome)
print ('Idade:', idade)
print ('Altura:', altura)
print ('Status Estudantil:', estudante)
