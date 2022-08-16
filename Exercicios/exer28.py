from random import randint
numero = int(input('digite um numero entre 0 e 5: '))
comp = randint(0, 5)
print()
if numero == comp:
    print('voce acertou')
else:
    print(f'Errou! tente novamente! {comp}')