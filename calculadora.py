import unittest

class Calculadora:
    def soma(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b

class Teste(unittest.TestCase):

    def setup(self):
        self.Calculadora = ('Calculadora')

    def teste_soma(self):
        self.calc = Calculadora()
        resultado = self.calc.soma(1, 2)
        esperado = 3
        self.assertEqual(resultado, esperado)

    def teste_sub(self):
        self.calc = Calculadora()
        resultado = self.calc.sub(18, 12)
        esperado = 6
        self.assertEqual(resultado, esperado)

    def teste_multi(self):
        self.calc = Calculadora()
        resultado = self.calc.mult(5, 5)
        esperado = 25
        self.assertEqual(resultado, esperado)

    def teste_div(self):
        self.calc = Calculadora()
        resultado = self.calc.div(24, 2)
        esperado = 12
        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
