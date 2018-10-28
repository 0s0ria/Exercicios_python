


class Calculador_de_impostos(object):

    def realizar_calculo(self, test):

        imposto_calculado = test.valor * 0.1
        print(imposto_calculado)

if __name__ == '__main__':

    from classe_privada import Test
    calculador = Calculador_de_impostos()
    test = Test(200)
    calculador.realizar_calculo(test)
