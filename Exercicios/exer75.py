tupla = (int(input(f'Número 1: ')), int(input(f'Número 2: ')), int(input(f'Número 3: ')), int(input(f'Número 4: ')))
print(tupla)
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 esta na posicao {tupla.index(3)+1}')
else:
    print('O valor 3 nao foi digitado: ')
print('Os valores pares digitados foram', end=' ')
for n in tupla:
    if n%2 == 0:
        print(n, end='')
