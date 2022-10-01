from time import sleep


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

def linha(tam=42):
    return '-'*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(46))
    print(linha())

def menu(lista):
    cabecalho('\033[95mMENU PRINCIPAL\033[m')
    c =1
    for item in lista:
        print(f'\033[1;90m{c}\033[m - \033[1;96m{item}\033[m')
        c+=1
    print(linha())
    opc = leiaint('\033[34mSua Opção:\033[m ')
    return opc

    
def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a= open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na craicao do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('\033[32mPESSOAS CADASTRADAS\033[m')
        for linha in a:
            dado = linha.split('-')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} \033[33manos\033[m')
        sleep(1)
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um Erro na abertura do arquivo!')
    else:
        try:
            a.write(f'\033[33m{nome}\033[m - \033[33m{idade}\033[m\n')
        except:
            print('houve um Erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de \033[30m{nome}\033[m adicionado')
            a.close()