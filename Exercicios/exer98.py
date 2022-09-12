from time import sleep

def contador(come, fim,pas):
    for c in range(come,fim,pas):
        sleep(0.5)
        print(c)
print('Contagem de 1 ate 10 de 1 em 1')
for c in range(1,11,1):
    sleep(0.5)
    print(c,end=' ')
print()
print('Contagem de 10 ate 0 de 2 em 2')
for c in range(10, 0, -2):
    sleep(0.5)
    print(c, end=' ')
print()

print('Agora é sua vez de persolazinar a contagem!! ')
come = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

contador(come, fim, pas)