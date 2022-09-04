dados = dict()
dados = {'nome':'pedro','idade':25}
print(dados['nome'])
dados['sexo']= 'M'#Adicionando novo vetor com valor
print('-='*15)
print(dados['sexo'])
del dados['idade']#Excluindo vetor inteiro
print('-='*15)
print(dados)
filmes = {'Titulo':'Star Wars','Ano':1997,'Diretor':'George Lucas'}
print('-='*15)
print(filmes.values())#Mostra o valor dos vetores
print('-='*15)
print(filmes.keys())#Mostra o nome dos vetroes
print('-='*15)
print(filmes.items())#mosta todos os valores juntos com os vetores
print('-='*15)
for c in filmes.items():
    print(c)
print('-='*15)
print(filmes)
print('-='*15)
for k, v in filmes.items():
    print(f'O {k} é {v}')
print('-='*15)
locadora = [{'Titulo':'Rick and Morty','Ano':2013,'Temporadas':6},{'Titulo':'Baki o Campeao','Ano':2018,'Temporadas':3},{'Titulo':'One Punch Man','Ano':2015,'Temporadas':2}]
for k, v in enumerate(locadora):
    print(f'o {k} é {v}')

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for c in brasil:
    for k, v in c.items():
        print(f' O campo {k} tem o valor {v}' )