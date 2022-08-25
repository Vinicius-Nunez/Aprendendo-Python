from random import randint
print(f'Sou seu computador\nAcabei de pensar em um numero entre 0 e 10...\nSera que voce consegue adivinhar qual foi?')
compu = randint(0,10)
tenta = 1
p = int(input('Digite seu palpite: '))
while not p == compu:
    tenta += 1
    if p < compu:
        print('Mais... Tente mais uma vez.')
        p = int(input('Qual é o seu palpite?'))
    elif p > compu:
        print('Menos... tente mais uma vez.')
        p = int(input('Qual é o seu palpite?'))
print(f'Acertou na {tenta} tentativa, parabens')