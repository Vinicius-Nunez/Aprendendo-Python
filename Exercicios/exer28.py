from random import randint
from time import sleep
numero = int(input('digite um numero entre 0 e 5: '))
comp = randint(0, 5)
print('Processando...')
sleep(1.5)
if numero == comp:
    print('voce acertou')
else:
    print(f'Errou! tente novamente! {comp}')