s = str(input('Dgite seu Sexo [M\F]: ').upper().strip()[0])
while s not in 'MF':
    s = str(input('dados invalidos. por favor, informe seu sexo: ').strip().upper()[0])
print(f'sexo {s} registrado com sucesso: ')

'''s = str(input('Digite seu sexo [M/F]: ')).upper()
while s != 'M' or s != 'F':
    if s == 'M' or s == 'F':
        break
print(f'Dado registrados')'''