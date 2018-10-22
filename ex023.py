# metodo por string

num = int( input('informe um numero: ')) # informa um numero
n = str(num) #converte ele para string

print('analisando numero {}'.format(num))
print('unidade {}'.format(n[3])) # mostra numero somente em sua 4 casa

print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))
