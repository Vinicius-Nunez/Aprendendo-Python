'''dados = ['vinicius', 25]
pessoas = []
dados2 = ['gustavo', 24]
pessoas.append(dados2[:])
pessoas.append(dados[:])
print('-='*30)
for c in pessoas:

    print(c[0])
print('-='*30)
print(pessoas)'''

galera = []
dados = []
totmai = totmen = 0
for c in range(0,3):
    dados.append(str(input('nome ')))
    dados.append(int(input('Idade')))
    galera.append(dados[:])
    dados.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} pessoas maiores de idade e {totmen} pessoas menores de idade ')