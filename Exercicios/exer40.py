nota= float(input('Digite uma nota: '))
nota2 = float(input('digite a segunda nota: '))
nota3 = float(input('digite a terceira nota: '))
res = (nota + nota2 + nota3) / 3
if res < 5.0:
    print(f'Sua media foi {res:.2f} e \033[1;41mvoce foi reprovado!\033[m')
elif res >= 5.0 and res <= 6.9:
    print(f'Sua media foi {res:.2f} e \033[1;43mvoce esta de recuperacao!\033[m')
else:
    print(f'Sua media foi {res:.2f} e foi\033[1;42mAPROVADO!\033[m')