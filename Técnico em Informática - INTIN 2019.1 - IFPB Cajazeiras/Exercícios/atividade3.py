#JOSEPH NICHOLLAS ABREU CAVALCANTE
def despesa (preco,distancia):
    return((distancia/14)*preco)

distancia = float(input("Qual a distancia?:"))
preco = float(input("Qual o preço da gasolina?:"))

print('a despesa é de',despesa(distancia,preco))
