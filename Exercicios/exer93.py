carreira = dict()
total = list()
carreira['nome']= str(input('Nome do jogador: '))
num = int(input(f'Quantas partidas {carreira["nome"]} jogou? '))
for c in range(1,num+1): 
    total.append(int(input(f'Quantos gols na partida {c}: ')))
    gols=sum(total)
carreira['gols']=total
carreira['total']=gols
print('-='*25)
print(carreira)
print('-='*25)
for k, v in carreira.items():
    print(f'O campo {k} tem o valor: {v}')
print('-='*25)
print('-='*3, f'O Jogador {carreira["nome"]} jogou {num} partidas','=-'*3)
for c, i in enumerate(total):
    print(f'   => Na partida {c+1} ele fez {i} gols ')
print('-='*25)
print(f'Foi um total de {gols} gols.')