#JOSEPH NICHOLLAS ABREU CAVALCANTE
def funcao(a,b,c):
    delta=b**2 - 4*a*c
    return raizes(funcao)
def raizes(delta_):
    if (delta_>0):
        return ('há duas raízes reais e distintas')
    elif(delta_==0):
        return ('há só uma raiz real')
    elif(delta_<0):
        return ('não há raiz real')
a=input('digite o valor de A')
b=input('digite o valor de B')
c=input('digite o valor de C')
print(raizes(delta))
