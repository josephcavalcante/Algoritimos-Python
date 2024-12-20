#JOSEPH NICHOLLAS ABREU CAVALCANTE
def funcao (numero):
    if (numero>0):
        return('positivo')
    elif(numero<0):
        return('negativo')
    elif (numero==0):
        return('neutro')
numero=int(input('digite seu número inteiro:'))
print(funcao(numero))
