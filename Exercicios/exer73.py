times = ('Corinthians','Palmeiras','Santos','Chapecoense','São Paulo','Portuguesa','Flamengo','Fluminense', 'Vasco', 'Red Bull')
print('-'*30)
print('Lista de times do Brasileirao: ')
for todos in times:
    print(todos, end='. ')
print('\n','-'*30)
print('Os cinco primeiros times sao:', end=' ')
for nomes in times[0:5]:
    print(nomes, end='. ')
print('\n','-'*30)
print('\nOs quatro ultimos sao: ', end=' ')
for ultimo in times[-5:-1]:
    print(ultimo, end='. ')
print('\n','-'*30)
print('\nTime em ordem alfabetica: ')
print(sorted(times))
print('\n','-'*30)
print(f'A chapecoense esta na posicao', end=' ')
print(times.index('Chapecoense')+1)

