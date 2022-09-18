def leiaint(num):
    ok = False
    valor= 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            valor = int(n)
            ok = True
            return n
        else:
            print('\033[0;31mERRO! digite um numero inteiro valido.\033[m')
        if ok:
            break
       
n = leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')