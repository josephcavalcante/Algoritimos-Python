#Joseph Nichollas Abreu Cavalcante

# 3.Peça ao usuário para inserir um ano e verifique se ele é bissexto. 
# Um ano é bissexto se for divisível por 4, mas não por 100, exceto se também for divisível por 400.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")