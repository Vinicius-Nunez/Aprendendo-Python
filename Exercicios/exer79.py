lista = []
while True:
    n = (int(input('Digite um valor: ')))
    
    if n not in lista:
        lista.append(n)
        print('Valor Adicionado!')
    else:
        print('Valor duplicado')
    cont = str(input('QUer continuar? [S/N]').strip().upper()[0])
    if cont == 'N':
        break
lista.sort()
print(f'Os valores adicionados foram {lista}')