# metodo metematico

num = int( input('informe um numero: ')) # informa um numero

# divisão inteira pela casa e depois se faz o mode de 10

u = num // 1 % 10
d =  num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# mostrar respostas

print('analisando numero {}'.format(num))

print('unidade {}'.format(u))

print('dezena {}'.format(d))

print('centena {}'.format(c))

print('milhar {}'.format(m))
