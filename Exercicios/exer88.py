from random import randint
from time import sleep
lista = []
jogos = []
print('-'*30)
print('      JOGA NA MEGA SENA      ')
print('-'*30)
n = int(input('Quantos jogos da mega voce quer?: '))
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont +=1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*3, f'SORTEANDO {n} JOGOS ','=-'*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}:{l}')
    sleep(0.8)
print('-='*5, f'BOA SORTE', '=-'*5)


    