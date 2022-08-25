num = int(input('Digite um numero: '))
razao= int(input('Digite os passos: '))
temp = num + (10-1) * razao
while num < temp+1:
    print(f'{num}', end='')
    print(' > ' if num < razao*10 else ' ', end='')
    num+= razao   