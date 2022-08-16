from random import randint
velo= randint(75, 90)
if velo > 80:
    multa=(velo-80)*7
    print(f'{velo}Km velocidade acima do limite da via permitido! Voce foi multado no valor de Rs{multa}')
else:
    print('Velocidade no limite permitido, tenha uma boa viagem!')