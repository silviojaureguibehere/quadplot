import math
from quadratic import Quadratic

#values
a = int(input ("value of a: "))
b = int(input ("value of b: "))
c = int(input ("value of c: "))

q1 = Quadratic(a, b, c)

#main equation
print (f"the polinomical form is: {q1.polinomicForm()}")
print (f"the factored form is: {q1.factoredForm()}")
print (f"the canonical form is: {q1.canonicalForm()}")
