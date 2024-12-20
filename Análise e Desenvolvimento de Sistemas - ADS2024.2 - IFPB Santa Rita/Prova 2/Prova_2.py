#Joseph Nichollas Abreu Cavalcante

# Faça um programa em python que receba e liste salários de profissionais na área de TI contendo o seguinte menu:
# 1. Adicionar Salário (10 pontos)
# 2. Listar Salários (20 pontos)
# 3. Soma total dos salários (10 pontos)
# 4. Média Salarial (20 pontos)
# 5. Mediana dos salários (10 pontos)
# 6. Dados de salários (20 pontos)
# 7. Remover salário (10 pontos)
# 8. Sair
# - Ao informar o item um, o usuário deve ser solicitado a informar um salário e fornecer esse valor (float).
# - Ao informar o item dois, o programa deve imprimir a lista de salários digitados.
# - No item 3, o programa deve imprimir a soma de todos os salários informados.
# - No item 4, o programa deve imprimir a média salarial dos salários informados.
# - No item 5, o programa deve informar a mediana dos salários.
# - No item 6, o programa deve informar o menor salário e o maior salário.
# - No item 7, o programa deve solicitar o salário a ser removido e remover.

salarios=[]
while True:
    print('''
          =======================
                   MENU
          =======================
          1. Adicionar Salário
          2. Listar Salários 
          3. Soma Total dos Salários 
          4. Média Salarial 
          5. Mediana dos Salários 
          6. Dados de Salários 
          7. Remover Salário 
          8. Sair''')
    
    operacao=(input('Digite qual operação você deseja fazer: '))
    
    if operacao=='1':
        adicionar = float(input('Digite um salário (O valor deve ser float): '))
        if adicionar < 0:
            print("O salário não pode ser negativo.")
        else:
            salarios.append(adicionar)
            print('Salário adicionado com sucesso!')
            
    elif operacao=='2':
        if not salarios:
            print('Não há nenhum salário para ser exibido!')
        else:
            print('Aqui está a lista com todos os Salários:')
        for i, valor in enumerate(salarios, 1):  
            print(f"{i}. R$ {valor:.2f}")
    elif operacao=='3':
        if not salarios:
            print('Não há nenhum salário para ser feito a soma!')
        else:
            print(f'Aqui está a soma total dos salários: {sum(salarios):.2f}')
    elif operacao=='4':
        if not salarios:
            print('Não há nenhum salário para ser feito a média!')
        else:
            print(f'Aqui está a média salarial: {(sum(salarios)/len(salarios)):.2f}')
    elif operacao=='5':
        if not salarios:
            print('Não há salários para calcular a mediana!')
        else:
            salarios_ordenados = sorted(salarios)
            numero = len(salarios_ordenados)
            if numero % 2 == 1:  
                mediana = salarios_ordenados[numero // 2]
            else:  
                numero_meio = numero // 2
                mediana = (salarios_ordenados[numero_meio - 1] + salarios_ordenados[numero_meio]) / 2
            print(f'Mediana dos salários: R$ {mediana:.2f}')
    elif operacao=='6':
        if not salarios:
            print('Não há salários para exibir os dados!')
        else:
            print(f"Maior salário: R$ {max(salarios):.2f}")
            print(f"Menor salário: R$ {min(salarios):.2f}")
    elif operacao=='7':
        buscar=float(input('Digite o Salário que você queira remover: '))
        if not salarios:
            print('Não há nenhum salário para ser removido!')
        else:
            if buscar in salarios:
                salarios.remove(buscar)
                print('Salário removido com sucesso!')  
            else:
                print('O salário não está salvo')   
    elif operacao=='8':
        print("Encerrando o programa.")
        break  
        
    else:
        print('Operação inválida, tente novamente!')
    