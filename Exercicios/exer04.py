# Trabalhando Objeto com Metodos.
n = input('digite algo: ')
print(f'O tipo primitivo desse valor é',{type(n)})
print(f'So tem espaços?',n.isspace())
print(f'É um numero?',n.isnumeric())
print(f'É alfabetico?',n.isalpha())
print(f'É alfanumerico?',n.isalnum())
print(f'Em maiuscula?',n.isupper())
print(f'Em minuscula?',n.islower()) 
print('Ésta capitalizada?', n.istitle())