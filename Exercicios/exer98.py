from time import sleep

def contador(come, fim, passos):
    if come <= fim:
        for c in range(come,fim+1,passos):
            sleep(0.2)
            print(c, end=' ')
    else:
        for c in range(come,fim-1,passos):
            sleep(0.2)
            print(c, end=' ')

print('-'*30)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1,11,1):
    sleep(0.2)
    print(c,end=' ')
print()
print('-'*30)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    sleep(0.2)
    print(c, end=' ')
print()
print('-'*30)

contador(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passos: ')))