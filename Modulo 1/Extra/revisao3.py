caixa_eletronico=1000
mostre = 0
while True:

    menu=print('(1) Sacar, (2) Depositar, (3) Ver Saldo e (4) Sair')
    mostre=int(input('escolha uma opção'))
    if mostre == 1:
        sacar=int(input('qual valor gostaria de sacar?'))
        caixa_eletronico-=sacar
        print(caixa_eletronico)
    elif mostre == 2:
        depositar=int(input('qual sera o valor depositado?'))
        caixa_eletronico+=depositar
        print(caixa_eletronico)
    elif mostre == 4:
        break
    else:
        print(caixa_eletronico)