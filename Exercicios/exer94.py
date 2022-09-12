dados = dict()
db = list()
fem= list()
media = list()
total= medi = 0
while True:
    dados.clear()
    dados['nome']=str(input('Nome: '))
    dados['sexo']=str(input('Sexo: [M/F] ').strip().upper()[0])
    while dados['sexo'] not in 'MF':
        print('Erro! Digite apenas M ou F..')
        dados['sexo']=str(input('Sexo: [M/F] ').strip().upper()[0])
    dados['idade']=int(input('Idade: '))
    perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    db.append(dados.copy())
    if dados['sexo'] == 'F':
        fem.append(dados['nome'])
    total += dados['idade']
    medi = total/len(db)
    while perg not in 'SN':
        print('Erro! Digite apenas S ou N..')
        perg = str(input('Quer continuar? [S/N] ').strip().upper()[0])
    if perg == 'N':
        break

print('-='*25)
print(f'A)    Temos o total de {len(db)} cadastradas.')
print(f'B)    A media de idade é de {medi:.2f} anos>')
print(f'C)    As mulheres cadastradas foram',end=' ')
for c in fem:
    print(c, end=' ')
for e in db:
    if e['idade'] >= medi:
        print('    ', end='')
        for k, v in e.items():
            print(f'{k} = {v};', end=' ')
        print()
print('<<< ENCERRADO >>>')
print(db)
