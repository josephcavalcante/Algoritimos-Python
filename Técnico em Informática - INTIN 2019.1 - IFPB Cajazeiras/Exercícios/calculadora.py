def soma(valor_1,valor_2):
    resultado_soma = valor_1 + valor_2
    return resultado_soma
def subtracao(valor_1,valor_2):
    resultado_subtracao = valor_1 - valor_2
    return resultado_subtracao
def multiplicacao (valor_1,valor_2):
    resultado_multiplicacao = valor_1 * valor_2
    return resultado_multiplicacao
def divisao (valor_1,valor_2):
    resultado_divisao = valor_1 / valor_2
    return resultado_divisao
while True:
    operacao = input('''
    quais das operações  desejas fazer?
    + (soma)
    - (subtração)
    * (multiplicação)
    / (divisão)
    sair
    ''')
    if ( operacao=='sair'):
        break
    valor_1 = int(input('digite o valor do primeiro valor: '))
    valor_2 = int(input('digite o valor do segundo valor: '))
    if (operacao=='+'):
        print(soma(valor_1,valor_2))
    elif (operacao=='-'):
        print(subtracao(valor_1,valor_2))
    elif (operacao=='*'):
        print(multiplicacao(valor_1,valor_2))
    elif (operacao=='/'):
        print(divisao(valor_1,valor_2))
    elif ( operacao=='sair'):
        break
