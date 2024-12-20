# Joseph Nichollas Abreu Cavalcante

# 1.Faça um programa em python onde você cria três variáveis (a, b, e c) e atribui a elas os valores 5, 10 e 15, respectivamente. 
# Em seguida, faça a receber o valor de b, b receber o valor de c, e c receber o valor de a + b.

a = 5
b = 10
c = 15

print("Valores iniciais:")
print(f"a = {a}, b = {b}, c = {c}")


a = b  
b = c  
c = a + b  

print("\nValores após as trocas:")
print(f"a = {a}, b = {b}, c = {c}")