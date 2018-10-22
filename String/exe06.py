#requeisitos
#lista
#for range
#split
#for in
#slice
#trocar primera letra para maiusculo

nome =  'leonardo fernando macena alves'

print(nome)

nome = nome.split()

print(nome)

for  i in range(len(nome)):
    nome[i] = nome[i].replace(nome[i][:1], nome[i][:1].upper())
    print(nome[i])

NAME = ''
for i in nome:
    NAME = NAME + i + ' '
    print(NAME)

print(NAME)
