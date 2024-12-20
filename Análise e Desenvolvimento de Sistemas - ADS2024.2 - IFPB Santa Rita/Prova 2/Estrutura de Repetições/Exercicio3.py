#Joseph Nichollas Abreu Cavalcante

# 3. Escreva um programa que peça dois números inteiros a e b (sendo a<b)
# e exiba todos os números ímpares entre eles. Utilize uma estrutura de repetição.

a = int(input("Digite o valor de a (menor número): "))
b = int(input("Digite o valor de b (maior número): "))

if a < b:
    print(f"\nNúmeros ímpares entre {a} e {b}:")
    
    for num in range(a + 1, b):
        if num % 2 != 0:
            print(num)
else:
    print("\nErro: Certifique-se de que a < b.")