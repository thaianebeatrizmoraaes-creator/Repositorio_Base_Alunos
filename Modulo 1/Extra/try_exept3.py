#Peça ao usuário um índice e tente acessar um elemento em uma lista predefinida (ex: [10,
#20, 30]). Use try-except para tratar IndexError (índice fora do intervalo) e ValueError (se o
#índice não for um inteiro). Exiba mensagens específicas para cada erro.


LISTA=[10, 20, 30, 40, 50]
try:
    num=int(input('digite um numero'))
    print(LISTA[num])

except:
    print('errou burro! 😂😂')