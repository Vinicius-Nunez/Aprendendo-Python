compras = ('Pão', 5.35,
          'Queijo', 6.47,
          'Aveia', 10.20,
          'Ovo', 15,
          'leite', 4.49,
          'chocolate', 5.34,
          'cigarro', 9.89,
          'sonho', 3.50,
          'bolo', 8.79,)
for item in range(0, len(compras)):
    if item %2 == 0:
        print(f'{compras[item]:.<30}', end=' ')
    else:
        print(f'R${compras[item]:>6.2f}')
