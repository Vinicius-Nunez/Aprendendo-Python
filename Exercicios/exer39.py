from datetime import date

ano = int(input('Digite o ano de nascimento: '))
idade= date.today().year-ano
if idade <18:
    print(f'Voce ainda vai se alistar! faltam {idade-18} para se alistar')
elif idade == 18:
    print(f'Voce esta na idade do alistamento obrigatoria, Va se alistar! ')
else:
    print(f'Voce ja passou da idade do alistamento obrigatorio! passaram-se {idade-18} anos')

