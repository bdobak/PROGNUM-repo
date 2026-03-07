from numpy import sin, cos, exp, pi
#making the monte carlo integration
n=10000
def montecarlo(func, n):
    vals=np.random.uniform(0,pi,n)
    total=0
    for x in vals:
        total+=eval(func)
    return total*pi/n
#getting the function without errors
while True:
    try:
        s=input("Give me a function of x: ")
        print("The integral of this function from 0 to pi is",montecarlo(s,n))
        break
    except NameError:
        print("The function is invalid, only use x as a variable")
    except ZeroDivisionError:
        print("The function is invalid, don't divide by zero")
    except TypeError:
        print("The function is invalid, only use valid operators")

f='x**4+np.exp(sin(x)+cos(x))'
print("The integral of f(x) from 0 to pi is ", montecarlo(f,n))