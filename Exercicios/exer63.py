num = int(input('Dgite quantos termos quer mostrar: '))
b = c = 0 
a = cont = 1
while cont <= num:
    print(f'{c} >', end=' ')
    c = a + b
    a = b
    b = c
    cont +=1
print('FIM')  