from random import randint
from time import sleep
from operator import itemgetter
lista = list()
num = randint(1,6)
num2 = randint(1,6)
num3 = randint(1,6)
num4 = randint(1,6)
dados = {'vini tirou':num, 'Guh tirou':num2, 'Rafa tirou':num3, 'Caique tirou':num4}
print('=-'*15)
ranking = dict()
for k,v in dados.items():
    print(f'{k} {v} no dado')
    sleep(0.5)
ranking = sorted(dados.items(), key=itemgetter(1), reverse=True )
print('-='*2, 'RANKING DOS JOGADORES', '=-'*2)
for i, v in enumerate(ranking):
    print(f' Em {i+1}º lugar: {v[0]} {v[1]}')
    sleep(1)