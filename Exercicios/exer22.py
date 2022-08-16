nome= input('digite seu nome:')
print(nome)
print('seu nome em maiuscula', (nome.upper()))
print('seu nome em minuscula', (nome.lower()))
vetor= nome.replace(' ','')
uau= nome.split()
print('quantas letras tem o seu primeiro nome', (len(uau[0])))
print('quantas letras tem o seu nome sem espaco', (len(vetor)))


