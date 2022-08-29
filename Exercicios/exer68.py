from random import randint

vitoria = 0
while True:
    computador = randint(0, 20)
    num = int(input('Digite um valor: '))
    opcao = str(input('Par or Impar?[P/I]').strip().upper()[0])
    resu = num + computador
    if opcao == 'P':
        opcao = 'PAR'
    else:
        opcao= 'IMPAR'
    if resu %2 == 0:
        resu =('PAR') 
    else: 
        resu =('IMPAR')

    if opcao == resu :
        vitoria += 1
        opcao =str('Ganhou!')
        print(f'Voce escoleu {num} e o computador {computador}, a soma dos numeros deu {resu}')
        print(f'Voce {opcao} e voce venceu {vitoria} vezes')
    else:
        opcao =str('Perdeu!')
        break
print(f'Voce escoleu {num} e o computador {computador}, a soma dos numeros deu {resu}')
print(f'Voce {opcao} e voce venceu {vitoria} vezes')

'''from random import randint
from time import sleep

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    opcao = str(input('[PAR/IMPAR]: ').upper().strip())
    computador = randint(1,20)
    soma = jogador + computador # RESPOTA IMPAR / PAR (STR)
    som = jogador + computador # SOMA IMPAR / PAR (INT)
    sleep(1)
    if soma %2 == 0: #PAR / IMPAR
        soma = str('PAR')

    else:
        soma = str('IMPAR')

    if opcao == soma: #GANHOU / PERDEU
        opcao = str('GANHOU!')

    else:
        opcao = str('PERDEU!')
    print('Hum........')
    sleep(0.5)
    print(f'Você jogou {jogador}\nComputador jogou {computador}\nA soma deu \033[36m{som}\033[m -> {soma}\nVocê \033[33m{opcao}\033[m')
    sleep(0.8)
    if opcao == 'PERDEU!':
        print('=-'*20)
        sleep(1)
        print(f'\033[31mGAME OVER!!!\033[m Você venceu \033[32m{vitorias}\033[m vezes')
        print('=-'*20)
        break
    vitorias += 1
sleep(0.5)
print('FIM')'''


'''from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    opcao = str(input('[PAR/IMPAR]: ').upper().strip())
    computador = randint(1,20)
    soma = jogador + computador
    if soma %2 == 0:
        soma = par = str('PAR')
    else:
        soma = impar = str('IMPAR')

    if opcao == soma:
        opcao = vitoria = str('GANHOU!')
    else:
        opcao = derrota = str('PERDEU!')
    print(f'Você jogou {jogador}\nComputador jogou {computador}\nA soma deu {soma}\nVocê {opcao}')
    if opcao == 'PERDEU!':
        print('=-'*20)
        print(f'GAME OVER, Você venceu {vitorias} vezes')
        print('=-'*20)
        break
    vitorias += 1
print('FIM')'''

'''from random import randint
from time import sleep

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)
vitorias = 0
while True:
    try:
        jogador = int(input('Diga um valor: '))
    except:
        pass
    try:
        opcao = str(input('[P/I]: ').upper().strip()[0])
    except:
        pass
    computador = randint(1,20)
    soma = jogador + computador # RESPOTA IMPAR / PAR (STR)
    som = jogador + computador # SOMA IMPAR / PAR (INT)
    sleep(1)
    if soma %2 == 0: # P/I
        soma = str('P')
    elif soma %2 == 1: #Faz o else não ser bugado no game
        soma = str('I')

    if opcao == soma: # GANHOU/PERDEU
        opcao = str('GANHOU!')
    else:
        opcao = str('PERDEU!')

    if soma == 'P': # SOMA VALENDO PAR E IMPAR DE NOVO PARA FACILITAR A VIDA DO USUARIO
        soma = 'PAR'
    elif soma == 'I':
        soma = 'IMPAR'
    print('Hum........')
    sleep(0.5)
    print(f'Você jogou {jogador}\nComputador jogou {computador}\nA soma deu \033[36m{som}\033[m -> {soma}\nVocê \033[33m{opcao}\033[m')
    sleep(0.4)
    if opcao == 'PERDEU!':
        print('=-'*20)
        sleep(0.5)
        print(f'\033[31mGAME OVER!!!\033[m Você venceu \033[32m{vitorias}\033[m vezes')
        print('=-'*20)
        break
    vitorias += 1
sleep(1)
print('FIM')'''