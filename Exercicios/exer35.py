r1 = float(input('Lado 1: '))
r2 = float(input('Lado 2: '))
r3 = float(input('Lado 3: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('Pode formar um triangulo!')
else:
    [ print('Não pode formar um triangulo!')]