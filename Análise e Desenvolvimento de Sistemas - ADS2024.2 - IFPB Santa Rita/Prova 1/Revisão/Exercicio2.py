#Joseph Nichollas Abreu Cavalcante

# 2.Crie uma calculadora, onde as entradas são:
# O primeiro valor
# O segundo valor
# A operação (+, -, *,/)
# A saída do programa deve ser o resultado da operação. 
# Caso o usuário digite um operador inválido, imprima a mensagem “operador inválido”.


n1 = float(input("Digite o primeiro valor: "))
n2 = float(input("Digite o segundo valor: "))
operacao = input("Digite a operação (+, -, *, /): ")


if operacao == "+":
    resultado = n1 + n2
    print("Resultado:", resultado)
elif operacao == "-":
    resultado = n1 - n2
    print("Resultado:", resultado)
elif operacao == "*":
    resultado = n1 * n2
    print("Resultado:", resultado)
elif operacao == "/":
    if n2 != 0:  
        resultado = n1 / n2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operador inválido.")