from math import sqrt


def fatorial(n):#Faz o fatorial de 'n'
    f = 1
    for c in range(n,0,-1):
        f*=c
        print(c, end='-')
    return f

def dobro(n):#Faz o dobro do de 'n'
    res = n*2
    return res

def raiz(n):#Faz a raiz quadrada de 'n'
    res = sqrt(n)
    return res

def metade(n):#Divide na metade o numero 'n'
    res = n/2
    return res

def aumento(preco, taxa=10):#Acrescenta a taxa que o usuario quiser e aplica encima do valor de 'preco'
    res = preco + preco * (taxa/100)
    return res
    

def diminuir(preco, taxa=10):#Diminui a taxa que o usuario quiser e aplica encima do valor de 'preco'
    res = preco - preco * (taxa/100)
    return res

