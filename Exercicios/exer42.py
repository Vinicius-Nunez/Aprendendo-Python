r1 = float(input('Lado 1: '))
r2 = float(input('Lado 2: '))
r3 = float(input('Lado 3: '))
if r1 + r2 >r3 and r2 + r3> r1 and r3 + r1 > r2:
    if r1 == r2 == r3:
        print('Pode formar um triangulo Equilátero!')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('pode formar um triangulo Isósceles!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('pode formar um triangulo Escalene!')
else:
     print('nao pode formar um triangulo!')
