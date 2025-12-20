import math

class Quadratic:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        self._xv = -b / 2*a
        self._yv = a * self._xv ** 2 + b*self._xv + c
        root = b ** 2 - 4*a*c
        if root >= 0:
            self._root1 = (-b + math.sqrt(root)) /2*a
            self._root2 = (-b - math.sqrt(root)) /2*a
        else:
            self._root1 = None
            self._root2 = None

    def polinomicForm (self):
        return f"{self._a}.x^2 + {self._b}.x + {self._c}"
    
    def canonicalForm (self):
        return f"{self._a}.(x-{(self._xv)})^2-{(self._yv)}"
    
    def factoredForm (self):
        if self._root1 == None:
            return ""
        else:
            return f"{self._a}.(x-{(self._a)}).(x-{(self._b)})"

