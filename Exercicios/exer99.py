def analigueitor(*num):
    print('~'*45)
    print('Analizando os valores passados...')
    for c in num:
        print(c, end=' ')
    print(f' Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('~'*45)
analigueitor(5, 6, 8, 7, 3, 9)
analigueitor(5, 6, 8, 2, 7, 10, 7, 3)
analigueitor(1, 2, 3, 4)