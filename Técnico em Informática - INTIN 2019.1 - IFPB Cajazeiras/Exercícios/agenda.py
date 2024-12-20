#Joseph Nichollas Abreu Cavalcante@
contatos=[]
while True:
    print('=================')
    print('⠀⠀Agenda INTIN')
    print('=================')
    print('Menu de opções:')
    print('1-Cadastrar novo contato')
    print('2-Buscar contato')
    print('3-Alterar contato')
    print('4-Excluir contato')
    print('5-Listar todos os contatos')
    print('6-Sair')
    operacao=input('que operação deseja fazer?:')
    if (operacao=='1'):
        nome=input('diga o nome do contato')
        while nome in contatos:
            nome=input('error, contato já esta na agenda')
        contatos.append(nome)
        numero=input('digite o numero do favorecido')
        contatos.append(numero)
        print('contato registrado!')
    if (operacao=='2'):
        buscar=input('diga o nome do contato')
        while buscar not in contatos:
            buscar=input('O contato não está registrado na agenda')
            buscar=input('diga o nome do contato')
        for i in range(len(contatos)):
            if(buscar==contatos[i]):
                print(contatos[i],contatos[i+1])
    if (operacao=='3'):
        buscar2=input('diga o nome do contato')
        while buscar2 not in contatos:
            buscar2=input('O contato não está registrado na agenda')
        contato=input('diga o nome do novo contato')
        numero2=int(input('diga o numero do contato'))
        for i in range(len(contatos)):
            if(buscar2==contatos[i]):
                contatos[i]=contato
                contatos[i+1]=numero2
    if (operacao=='4'):
        delcontato=input('diga o nome do contato que deseja excluir')
        while delcontato not in contatos:
            delcontato=input('contato inexistente!!')
        for i in range(len(contatos)):
            if delcontato==contatos[i]:
                del contatos[i+1]
                del contatos[i]
                break
    if (operacao=='5'):
        for i in range(0,len(contatos),2):
            print(contatos[i],contatos[i+1])

    if (operacao=='6'):
        print('saindo...')
        break
