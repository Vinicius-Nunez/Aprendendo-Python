coisas = ('citroem',
          'honda',
          'toyota',
          'lexus',
          'fiat',
          'porsche',
          'ferrari',
          'koenigsegg',
          'pagani',
          'dodge',
          'mercedes' )
for c in coisas:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
        