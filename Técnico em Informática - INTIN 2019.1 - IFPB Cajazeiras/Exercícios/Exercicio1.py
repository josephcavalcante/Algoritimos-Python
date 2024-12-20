#JOSEPH NICHOLLAS ABREU CAVALCANTE
def funcao(idade):
    if (0<=idade<=12):
        return('criança')
    elif (12<=idade<=17):
        return('adolecente')
    elif (18<=idade<=59):
        return('adulto')
    elif (idade>=60):
        return('idoso')
    elif (idade<0):
        return('não existe')
idade=int(input('qual a idade da pessoa?'))
print(funcao(idade))
    
    

