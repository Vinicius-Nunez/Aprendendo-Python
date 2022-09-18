def ficha(n='<Desconhecido>',g=0):
    print(f'O jogador {n} fez {g} gols(s) no campeonato')

nome = str(input('Nome do jogador: '))
gols = str(input('Numeros de gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()== '':
    ficha(g=gols)
else:
    ficha(nome,gols)