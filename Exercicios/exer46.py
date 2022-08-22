from time import sleep
from emoji import emojize
n= int(input('Digite um numero: '))
for c in range(n, -1, -1):
    print(c)
    sleep(0.5)
print(emojize(':fire::fire::fire::fire:\033[31mbuuuuuuuuuuuuum\033[m:fire::fire::fire::fire:'))