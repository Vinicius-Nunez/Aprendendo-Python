num = int(input('Digite um numero: '))
razao= int(input('Digite os passos: '))
termo = num
cont =1
total = 0
mais = 10
while mais != 0: 
    total += mais
    while cont <= total:
        print(f'{termo}', end='')
        print(' > ' if num < razao*10 else '  Pause', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer mostrar a mais?: '))
print(f'Progressao finalizada com {total} Termos mostrados')