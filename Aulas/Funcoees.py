


from math import sqrt


def fatorial(n):
    f = 1
    for c in range(n,0,-1):
        f*=c
        print(c, end='x')
    return f

def dobro(n):
    res = n*2
    return res
    
def raiz(n):
    res = sqrt(n)
    return res