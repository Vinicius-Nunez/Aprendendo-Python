from math import sqrt
from time import sleep

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))
while True:
    print('[1]- Somar\n[2]- Multiplicar\n[3]- dividir\n[4]- Raiz\n[5]- Novos Numeros\n[6]- Sair')
    res= int(input('Escolha uma opcao a cima: '))
    if res == 1:
        soma = n1 + n2
        print(f'A soma deu {soma}')
        print('-=-'*10)
        sleep(1)
    elif res == 2:
        soma = n1 * n2
        print(f'A mulplicacao é {soma}')
        print('-=-'*10)
        sleep(1)
    elif res == 3:
        soma = n1/n2
        print(f'O valor da divisao é {soma}')
        print('-=-'*10)
        sleep(1)
    elif res == 4:
        soma = sqrt(n1)
        soma2 = sqrt(n2)
        print(f'a raiz quadrada do primeiro numero é {soma:.2f} e a do segundo é {soma2:.2f}')
        print('-=-'*10)
        sleep(1)
    elif res == 5:
        print('Digite os numeros novamentos! ')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif res == 6:
        print(f'S', end='') 
        sleep(0.8) 
        print(f'A', end='')
        sleep(0.8)
        print(f'I', end='')
        sleep(0.8)
        print(f'N', end='')
        sleep(0.8)
        print(f'D', end='')
        sleep(0.8)
        print(f'O...', end='')
        sleep(0.5)
        break
    else:
        print('Opcao invalida, tente novamente ')
        print('-=-'*10)
        sleep(1)