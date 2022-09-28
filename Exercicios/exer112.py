from funcoes.NFormatos import resumo
from funcoes.dados import leiadinheiro

num = leiadinheiro('Digite um valor: ')
taxa = int(input('Digite a taxa de aumento: '))
taxo = int(input('Digite a taxa de diminuicao: '))
resumo(num,taxa,taxo)