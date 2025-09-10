#Crie uma função chamada dividir(a, b) que retorne o resultado da divisão a / b.
#Utilize um bloco try-except genérico (sem especificar o tipo de exceção) para tratar
#quaisquer erros que possam ocorrer durante a operação (como divisão por zero ou tipos
#inválidos).
#Em caso de erro, a função deve retornar None.



try:
    NUM_1=int(input('digite um numero'))
    NUM_2=int(input('digite o segundo numero'))

    dividir=(NUM_1/NUM_2)
except:
   print('none')