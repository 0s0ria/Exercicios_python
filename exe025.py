# porgrama para usar uma palavra em um nome

nome = str(input('Digite seu nome completo: ')).strip() #strip para eliminar os espaços do começo e fim

print ('Seu nome tem silva: {}' .format('silva' in nome.lower())) # in verifica na variael se tem silva, e lower trnasforma todas as letras em minusculas
