idade=int(input('digite a idade'))
estudante=(input('você é estudante?'))
if idade <= 12:
    print('ingresso infantil: R$ 8,00')
elif idade > 13 and idade <64:
    print('ingresso adulto: R$ 20,00')    
else:
    print('ingresso idoso: R$ 10,00') 
if estudante == 'sim':
    print('ingresso estudante: R$ 12,00')