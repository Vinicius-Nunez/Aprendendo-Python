from time import sleep
from funcoes.menu import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:

    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('\033[32mNOVO CADASTRO\033[m')
        nome = str(input('nome: ').title())
        idade= leiaint('idade: ')
        cadastrar(arq, nome, idade)
    
    elif resposta == 3:
        sleep(0.3)
        cabecalho('\033[33mSaindo do sistema... Até logo!\033[m ')
        sleep(0.5)
        break
    
    else:
        print('\033[31mErro! Digite uma opção valida!\033[m')
    sleep(1)