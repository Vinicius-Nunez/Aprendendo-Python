num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[32m',end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print(f'\033[m o numero {num} foi divisivel {tot}')
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele nao é primo')