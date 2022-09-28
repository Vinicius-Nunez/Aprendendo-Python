def leiadinheiro(smg):
    valido = False
    while not valido:
        entrada = str(input(smg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum():
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            valido = True
            return float(entrada)

def leiaintt(num):
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

def leiafloat(num=0):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro!! por favor digite um numero real:\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[34mO usuario nao quis colocar esse numero.\033[m ')
            return 0
        else:
            return n

def leiaint(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('\033[31mErro!! por favor, digite um numero valido:\033[m ')
            continue
        except (KeyboardInterrupt):
            print('\033[34mO usuario nao quis colocar esse numero.\033[m ')
            return 0
        else:
            return n 