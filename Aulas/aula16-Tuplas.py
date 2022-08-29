lanche = ('carne', 'carvao', 'pao de aloho', 'bebida')
#print(sorted(lanche))#Sorted == Organiza a Tupla em ordem alfabetica!
for pos, comida in enumerate(lanche):#enumeate == mostra a posicao de cada valor!

    if comida == 'bebida':
        print(f'Eu tomei uma {comida} nao posicao {pos}')
    elif comida == 'carvao':
        print(f'Eu comprei um {comida} na posicao {pos}')
    else:
        print(f'Eu vou comer {comida} na posicao {pos}')
