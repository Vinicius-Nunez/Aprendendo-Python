lista =  []
listapar = []
listaimp = []
while True:
    n = int(input('Digite um valor: '))
    cont = str(input('Quer continuar? [S/N]: ').strip().upper()[0])
    lista.append(n)
    if n % 2 ==0:
        listapar.append(n)
    elif n % 2 ==1:
        listaimp.append(n)
    if cont == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista impar é {listaimp}')