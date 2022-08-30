numeros = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
cont= ' '
while True:
    qual= int(input('Digite um numero entre [0/20]: '))
    while qual <0 or qual >20:
        qual= int(input('Numero errado, Digite um numero entre [0/20]: '))
    print(numeros[qual])
    cont = str(input('Quer continuar?[S/N]').strip().upper()[0])
    if cont == 'N':
        break