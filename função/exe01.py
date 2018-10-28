#função simples


def soma (a,b):
    return a + b

n = soma(12, 20)
print(n)


def salario_liquido(salario, imposto = 0.05):
    return (salario - (salario * imposto))

if __name__ == '__main__':
    print(salario_liquido(1200))
