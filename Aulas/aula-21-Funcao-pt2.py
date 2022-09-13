help(len)#mostra a documentacao do metedo escolhido.
print(input.__doc__)#mostra a documentacao do metedo escolhido.
def contador(i, f, p):
    """_é um cantador de passos com inicio e fim_

    Args:
        i (_int_): _inicio da contagem_
        f (_int_): _fim da contagem_
        p (_int_): _passos_
    """
    c=i
    while c <= f:
        print(f'{c}', end=' ')
        c+=p
    print('Fim')
contador(2,10,2)
print(contador.__doc__)

def somar(a,b,c=0):
    """_FAz a soma de tres valores e mostra o resultado na tela_

    Args:
        a (_int_): _o primero valor_
        b (_int_): _o segundo valor_
        c (int, optional): _o terceiro valor_. Defaults to 0.
    """
    s=a+b+c
    print(f'A soma vale {s}')
somar(2,5,8)
somar(2,5)

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f
n = int(input('Digite um numero'))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

def par(num=0):
    if num%2==0:
        return True
    else:
        return False

num = int(input('Digite um numero: '))
if par(num):
    print('Par')
else:
    print('Impar')