'''import random
aluno= random.choice(['Gabriel', 'Enzo', 'Vinicius', 'Gustavo'])#random.choice pega um elemento aleatorio em uma lista.
print(f'{aluno}')'''
from random import choice, random
al1 = input('digite um nome: ')
al2 = input('digite um nome: ')
al3 = input('digite um nome: ')
al4 = input('digite um nome: ')
alunos = choice([al1, al2, al3, al4])
print(f'O aluno sorteado para apagar a lousa foi o {alunos}')