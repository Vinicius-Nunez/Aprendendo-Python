from random import randint, seed

valores = (randint(0,15),randint(0,15),randint(0,15),randint(0,15),randint(0,15))
print(valores)
print(f'O maior valor foi: {max(valores)}')
print(f'O menor valor foi: {min(valores)}')