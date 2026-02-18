from math import *
a=float(input('Enter a: '))
b=float(input('Enter b: '))
c=float(input('Enter c: '))
D=b**2-4*a*c
if D>0:
    x1=(-b+sqrt(b**2-4*a*c))/(2*a)
    x2=(-b-sqrt(b**2-4*a*c))/(2*a)
    print(f"The two solutions are {x1} and {x2}")
elif D==0:
    x=-b/(2*a)
    print(f"The solution is {x}")
else:
    print("There are no solutions")
