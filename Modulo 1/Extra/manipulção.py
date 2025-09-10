agenda=['Cleber','João','Maria','José','Gabriel']
while True:
    menu=print("(1) cadastrar pessoa \n(2) listar pessoa \n(3) excluir pessoa \n(4) sair ")
    opc= int(input('selecione uma opção'))

    if opc == 1:
        adc = input('digite o nome da pessoa: ')
        agenda.append(adc)
    elif opc == 2:
        print(agenda)
    elif opc == 3:
        rmv = input('digite o nome da pessoa: ')
        agenda.remove(rmv)
    else:
        print('='*50)
        break