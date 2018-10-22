# cores

cores = {'verde' : 'green', 'vermelho' : 'red', 'preto': 'black', 'branco': 'white' }

cor = str (input ('Escolha a cor q deseja traduzir: ' )).strip()

traducao = cores.get (cor.lower, 'Esta cor não consta no no meu dicionario')

print (traducao)
