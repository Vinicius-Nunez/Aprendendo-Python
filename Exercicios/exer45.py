from time import sleep
from random import choice
print('-=-'*25)
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('PO')
sleep(0.6)
print(' PEDRA, PAPEL, TESOURA....')
print('-=-'*25)
pessoa = str(input('Escolha uma das opcoes a cima! ').strip().upper())
comp = choice(['PEDRA', 'PAPEL', 'TESOURA'])
if pessoa == comp:
    print(f'EMPATE')
elif pessoa == 'PEDRA' and comp == 'TESOURA' or pessoa == 'TESOURA' and comp == 'PAPEL' or pessoa == 'PAPEL' and comp == 'PEDRA':
    print(f'VOCÊ GANHOU! Você escolheu: {pessoa} e o computador escolheu: {comp}')
else:
    print(f'VOCÊ PERDEU! Você escolheu {pessoa} e o computador escolheu {comp}')