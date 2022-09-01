lista = []
while True:
    lista.append(int(input('Digite um Numero: ').strip()))
    cont = str(input('Quer continuar? [S/N]: ' ).strip().upper()[0])
    if cont == 'N':
        break
print(f'Voce digitou {len(lista)} elementos na lsita')
lista.sort(reverse=True)
if 5 in lista:
    print('O valor 5 esta nalista!')
else:
    print('O valor 5 nao foi adicionado a lista!')
print(f'Os valores em ordem decrescente é {lista}')