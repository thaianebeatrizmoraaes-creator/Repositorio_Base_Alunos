lista=[1, -20, 14, 7, -12, 17, -25, 0, 10, 0]
contador_negativo=0
contador_positivo=0
contador_zero=0
for num in lista:
    if num >=1:
        print('positivo')
        contador_positivo +=1
    elif num == 0:
        print('zero')
        contador_zero +=1   
    else:
        print('negativo')
        contador_negativo +=1      
print(f'{contador_positivo} positivo')
print(f'{contador_zero} zeros')
print(f'{contador_negativo} negativos')