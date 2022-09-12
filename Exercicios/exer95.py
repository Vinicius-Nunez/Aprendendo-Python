jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome']= str(input('Nome do jogador: '))
    num = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(1,num+1): 
        partidas.append(int(input(f'Quantos gols na partida {c}: ')))   
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]').upper()[0])
    
    while resp not in 'SN':
        print('Erro! Apenas digite S ou N: ')
        resp = str(input('Quer continuar? [S/N]').upper()[0])
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! nao existe jogador com codigo {busca}! ')
    else:
        print(f' -- LEVANTAMENTO DE JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols')
    print('-='*35)
print('<<< VOLTE SEMPRE >>>')