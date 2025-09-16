# Usando o streamlit crie um site com 4 colunas em cada coluna você vai
# realizar uma operação
# Coluna 1: Somar
# Coluna 2: Dividir
# Coluna 3: subtrair
# Coluna 4: multiplicar
# Use o seu código como exemplo e abaixo vou colocar as funções que você
# vai utilizar
# Coluns
# text_input
# button
# int
# if e else

import streamlit as st

coluna = st.columns (4)
coluna [0].write("coluna 1")
coluna [1].write("coluna 2")
coluna [2].write("coluna 3")
coluna [3].write("coluna 4")

numero1=st.text_input('digite um numero')
numero2=st.text_input('digite o segundo numero')

with coluna[0]:

    if st.button(' soma '):
       resultado=int(numero1)+ int(numero2)
       st.text(f'o resultado é {resultado}')

with coluna[1]:

    if st.button(' subtração '):
       resultado=int(numero1) - int(numero2)
       st.text(f'o resultado é {resultado}')

with coluna[2]:

    if st.button(' multiplicação '):
       resultado=int(numero1) * int(numero2)
       st.text(f'o resultado é {resultado}')

with coluna[3]:

    if st.button(' divisão '):
       resultado=int(numero1) / int(numero2)
       st.text(f'o resultado é {resultado}')
