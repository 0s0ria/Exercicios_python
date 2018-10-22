# programa para verifica contas letras especificas tem

frase =  str (input('Digite sua frase: ')) . strip()

print('Contas vezes aparece a letra A na frase {}' .format(frase.lower().count('a'))) # count conta quantos tem

print('A primera letra A apareceu na posião {}' .format(frase.lower().find('a')+1)) # find progura e mostra a posiçao

print('A Ultima letra A apareceu na posião {}' .format(frase.lower().rfind('a')+1))# procura da direita para esquesda

print('contas letras tem a frase: {}'.format(len(frase))) # conta items na paralvra
