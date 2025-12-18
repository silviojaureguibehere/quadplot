import math

#values
a = int(input ("valor de a: "))
b = int(input ("valor de b: "))
c = int(input ("valor de c: "))

#main equation
print (f"la ecuacion principal es: {a}.x^2 + {b}.x + {c}")

#roots
root = b ** 2 - 4*a*c
rot = -b / 2*a

if root < 0:
    print ("no hay raices (no hay forma factorizada)")

else: 
    if root == 0:
        print ("la raiz es:" + rot + "(no hay forma factorizada)")
    else:
        a = (-b + math.sqrt(root)) /2*a
        b = (-b - math.sqrt(root)) /2*a

        print (f"la forma factorizada es: {a}.(x-{(a)}).(x-{(b)})")

#vertex
xv = -b /2*a
yv = a * xv ** 2 + b*xv + c

#result
print (f"la forma canonica es: {a}.(x-{(xv)})^2-{(yv)}")