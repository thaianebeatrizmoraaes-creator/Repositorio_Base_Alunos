# Exercício 1: Validação de Entrada Inteira

# Escreva um programa que solicite um número inteiro ao usuário. Use try-except para tratar
# entradas não numéricas e valores não inteiros. Se ocorrer um erro, peça a entrada
# novamente até que seja válida.

try:
   num=int(input('digite um numero:'))
except:
    print('numero errado, tente novamente')