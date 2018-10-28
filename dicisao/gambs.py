


while True:
    var = input(str('digite um numero: '))
    try:
        case = {
        '1': 'bixa',
        '2': 'viadao',
        '3': 'merda'
        }
        print(case[var])
    except:
        print('numero invalido')
