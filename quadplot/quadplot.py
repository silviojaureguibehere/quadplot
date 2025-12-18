import math

#values
a = int(input ("value of a: "))
b = int(input ("value of b: "))
c = int(input ("value of c: "))

#main equation
print (f"the main equation is: {a}.x^2 + {b}.x + {c}")

#roots
root = b ** 2 - 4*a*c
xv = -b / 2*a

if root < 0:
    print ("hasn´t roots (it hasn´t factored form)")

else: 
    if root == 0:
        print (f"the factored form is: {(a)}.(x-{(xv)}).(x-{(xv)})")
    else:
        a = (-b + math.sqrt(root)) /2*a
        b = (-b - math.sqrt(root)) /2*a

        print (f"the factored form is: {a}.(x-{(a)}).(x-{(b)})")

#vertex
yv = a * xv ** 2 + b*xv + c

#result
print (f"the canonical form is: {a}.(x-{(xv)})^2-{(yv)}")