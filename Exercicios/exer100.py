from random import randint


def sorteio(lista):
    for c in range(0,5):
        lista.append(randint(1,11))

def somapar(par):
    pari=0
    for c in par:
        if c%2==0:
            pari+=c
    return pari
numeros= list()
sorteio(numeros)
xun = somapar(numeros)
print('Sorteando 5 valores da lista: ', end='')
for c in numeros:
    print(c, end=' ')
print('PRONTO!!')
print(f'Somando os valores pares de {numeros}, Temos: {xun}')
