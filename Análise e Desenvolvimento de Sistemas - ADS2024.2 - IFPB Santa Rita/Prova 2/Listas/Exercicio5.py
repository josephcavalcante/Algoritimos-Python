#Joseph Nichollas Abreu Cavalcante

# 5. Peça ao usuário para inserir uma lista de  10 idades. 
# Utilize um loop para classificar as idades nas categorias abaixo, 
# contando quantas pessoas estão em cada categoria:
# Menor de 18 anos: "Menor de idade".
# Entre 18 e 59 anos: "Adulto".
# 60 anos ou mais: "Idoso".

lista=[]
lista_m=[]
lista_a=[]
lista_i=[]
for i in range(10):
   num=int(input('digite uma idade:'))
   lista.append(num) 
for i in lista:
    if i<18:
        lista_m.append(i)
    elif 18>=i<=59:
        lista_a.append(i)
    else:
        lista_i.append(i)
       
print('A quantidade de pessoas menor de idade:',len(lista_m))
print('A quantidade de pessoas adulta:',len(lista_a))
print('A quantidade de pessoas idosos:',len(lista_i))
