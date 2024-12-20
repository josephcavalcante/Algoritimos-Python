#JOSEPH NICHOLLAS ABREU CAVALCANTE
def maior(numero1,numero2,numero3):
    if(numero1>numero2,numero1>numero3):
        return('o numero maior é:',numero1)
    elif (numero2>numero1,numero2>numero3):
        return('o numero maior é:',numero2)
    elif (numero3>numero1,numero3>numero2):
        return ('o numero maior é:',numero3)
    elif(numero1==numero2,numero1==numero3):
        return ('está incorreto,os numeros são iguais')
    elif(numero2==numero1,numero2==numero3):
        return ('está incorreto,os numeros são iguais')
    elif(numero3==numero1,numero3==numero1):
        return ('está incorreto,os numeros são iguais')
    
def menor(numero1,numero2,numero3):
    if(numero1<numero2,numero1<numero3):
        return('o numero menor é:',numero1)
    elif(numero2<numero1,numero2<numero3):
        return ('o numero menor é:',numero2)
    elif (numero3<numero1,numero3<numero2):
        return ('o numero menor é:',numero3)
    elif(numero1==numero2,numero1==numero3):
        return ('está incorreto,os numeros são iguais')
    elif(numero2==numero1,numero2==numero3):
        return ('está incorreto,os numeros são iguais')
    elif(numero3==numero1,numero3==numero1):
        return ('está incorreto,os numeros são iguais')
numero1=int(input('digite o primeiro numero dinstinto:'))
numero2=int(input('digite o segundo numero dinstinto:'))
numero3=int(input('digite o terceiro numero dinstinto:'))
print(maior(numero1,numero2,numero3))
print(menor(numero1,numero2,numero3))
