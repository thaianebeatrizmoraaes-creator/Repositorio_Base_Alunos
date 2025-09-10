valor=float(input('digite o valor da compra'))
desconto= valor * 0.10
valorfinal=valor-desconto
if valor >= 100:
    print(valorfinal)
else:
    print(valor)    