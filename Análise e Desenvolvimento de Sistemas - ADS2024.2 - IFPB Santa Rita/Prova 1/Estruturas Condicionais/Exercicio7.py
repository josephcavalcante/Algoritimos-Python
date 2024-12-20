#Joseph Nichollas Abreu Cavalcante

# 7. Escreva um programa que peça ao usuário para digitar uma temperatura em graus Celsius e a converta para Fahrenheit. Exiba uma mensagem indicando se a temperatura está "Quente", "Moderada" ou "Fria" em Fahrenheit.
# Critérios: 
# Acima de 86°F é "Quente", entre 60°F e 86°F é "Moderada", e abaixo de 60°F é "Fria".
# celsius para farenheit -> celcius * 1.8 + 32

celsius = int(input('digite uma temperatura em Celsius:'))
fahrenheit =  celsius * 1.8 + 32
if fahrenheit > 86 :
    print('a temperatura está quente')
elif fahrenheit < 60 :
    print('a temperatura está fria')
else:
    print('a temperatura está moderada')