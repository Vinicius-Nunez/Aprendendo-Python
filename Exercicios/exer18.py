import math
angulo= float(input('digite um valor: '))
c= math.cos(math.radians(angulo))
print(f'O angulo de {angulo} tem o cosseno de {c:.2f}')
c= math.tan(math.radians(angulo))
print(f'O angulo de {angulo} tem a tangente de {c:.2f}')
c= math.sin(math.radians(angulo))
print(f'O angulo de {angulo} tem o seno de {c:.2f}')