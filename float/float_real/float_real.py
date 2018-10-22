

def FloatReal(num):
    n = str(num)
    if 'e' in n:
        if '-' in n:
            end = n.find('e') + 2
            case = int(n[end:])
            if '.' in n:
                start = n.find('.')
                number = n[:start + 1]
                for v in range (case):
                    number = number + '0'
                resto = n[(start+1):(end-2)]
                number = number + resto
                return number
    else:
        return n
