peso = float(input('DIGITE SEU PESO: '))
alt = float(input('Digite a sua altura: '))
imc = peso / alt **2
if imc < 18.5:
    print(f'Seu imc é {imc:.2f} esta a baixo do peso')
elif imc >= 18.5 and imc <= 25:
    print(f'seu imc é {imc:.2f} e esta com o peso idel ')
elif imc <=30:
    print(f'seu imc é {imc:.2f} e esta sobre peso')
elif imc <= 40:
    print(f'seu imc é {imc:.2f} e esta com obesidade ')
else:
    print(f'Seu imc é {imc:.2f} e esta com obesidade morbida!!!')