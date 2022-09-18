from time import sleep

c= ['\033[m' ,   #0 - Cor branca
    '\033[0;30;41m', #1 - cor vermelha
    '\033[0;30;43m', #2 - cor amarelo
    '\033[0;30;42m', #3 - cor verde
    '\033[7;97m', #4 - cor branco
    ];
def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 3)
    print(c[4], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)
    print(c[0], end='')
    sleep(1)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("funcao ou biblioteca>  "))
    if comando.upper()== 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATE LOGO!', 1)