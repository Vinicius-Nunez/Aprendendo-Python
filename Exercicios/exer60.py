num = int(input('Digite um numero: '))
soma = 1
while num >0:
    soma *= num
    print(f'{num}',end='')
    print(' x ' if num>1 else ' = ', end='')
    num = num - 1
    
print(soma)


