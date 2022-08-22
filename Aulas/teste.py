from rich import print
import os
Votos_Lula = 0 
Votos_Bolsonaro = 0


while True:
    print('-'*20)
    print(f'[on blue]Total Bolsonaro:[/] {Votos_Bolsonaro}{os.linesep}[on red]Total Lula:[/] {Votos_Lula}')
    print('-'*20)

    try:
        voto = int(input(f'Para quem gostaria de votar?{os.linesep} 1 - Lula{os.linesep} 2 - Bolsonaro{os.linesep}Seu voto: '))
        if voto == 1:
            Votos_Lula += 1
        elif voto == 2:
            Votos_Bolsonaro += 1
        else:
            pass
    except:
        print('Digite apenas 1 ou 2 para votar')
    os.system('cls')