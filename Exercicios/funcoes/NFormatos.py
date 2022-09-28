from math import sqrt
from funcoes.linhas import lin2, lin


def fatorial(n):#Faz o fatorial de 'n'
    f = 1
    for c in range(n,0,-1):
        f*=c
        print(c, end='-')
    return f

def dobro(preco, format = False):#Faz o dobro do de 'preco'
    res = preco*2
    return res if format == False else moeda(res)

def raiz(preco, format = False):#Faz a raiz quadrada de 'preco'
    res = sqrt(preco)
    return res if format == False else moeda(res)

def metade(preco, format = False):#Divide na metade o numero 'preco'
    res = preco/2
    return res if format == False else moeda(res)

def aumento(preco, taxa=10, format= False):#Acrescenta a taxa que o usuario quiser e aplica encima do valor de 'preco'
    res = preco + preco * (taxa/100)
    return res if format == False else moeda(res)
    

def diminuir(preco, taxa=10, format=False):#Diminui a taxa que o usuario quiser e aplica encima do valor de 'preco'
    res = preco - preco * (taxa/100)
    return res if format == False else moeda(res)

def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def resumo(preco, taxa, taxo):
    lin('RESUMO DO VALOR')
    print(f'Preço Analizado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{moeda(dobro(preco))}')
    print(f'Metade do preco: \t{moeda(metade(preco))}')
    print(f'Aumentando %{taxa}, temos: \t{moeda(aumento(preco,taxa))}')
    print(f'Diminuindo %{taxo}, temos: \t{moeda(diminuir(preco,taxo))}')
    lin2()
