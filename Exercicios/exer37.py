num= int(input('digite um numero: '))
print('[1] - Binario.\n[2] - Octal.\n[3] - Hexadecimal.')
opcao= int(input('Qual a sua opcao?: '))
if opcao == 1:
    print(bin(num))
elif opcao == 2:
    print(oct(num))
elif opcao == 3:
    print(hex(num))
else:
    print('Opcao errada!! tente novamente')

