from quadplot.quadratic import Quadratic
import unittest

class TestQuadratic(unittest.TestCase):

    def test_polinomicForm(self):
        sut = Quadratic(1, 2, 3)
        polinomicForm = sut.polinomicForm()
        self.assertEqual (polinomicForm, "1.x^2 + 2.x + 3", "The polinomic form is wrong")

    def test_canonicalForm(self):
        sut = Quadratic(1, 2, 3)
        canonicalForm = sut.canonicalForm()
        self.assertEqual (canonicalForm, "1.(x--1.0)^2-2.0", "The canonical form is wrong")

    def test_factoredFormReal(self):
        sut = Quadratic(1, 3, 2)
        factoredForm = sut.factoredForm()
        self.assertEqual (factoredForm, "1.(x-1).(x-3)", "The factored form is wrong")

    def test_factoredFormImaginary(self):
        sut = Quadratic(1, 2, 3)
        factoredForm = sut.factoredForm()
        self.assertEqual (factoredForm, "", "The factored form is wrong")

if __name__ == '__main__':
    unittest.main()

