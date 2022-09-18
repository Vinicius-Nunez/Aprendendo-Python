def fatorial(num, show=False):
    """_fatorial com escolhas, se quer mostrar a equacao ou apenas o resultado_

    Args:
        num (_int_): _valor para fazer o fatorial_
        show (bool, optional): _opcao de mostrar a equacao ou apenas o resultado_. Defaults to False.

    Returns:
        _int_: _retorna o valor pedido_
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print('=', end='')
        f*=c
    return f
n = int(input('Digite um numero'))
print(fatorial(n, True))