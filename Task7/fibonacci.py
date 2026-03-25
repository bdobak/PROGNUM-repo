class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self):
        self.fib=[0,1]
    def func1(self,N):
        fib=self.fib
        while len(fib)<N:
            fib.append(fib[-1]+fib[-2])
        return fib[-1]

    def func2(self,N,M):
        fib=self.fib
        while len(fib)<N:
            fib.append(fib[-1]+fib[-2])
        divs=[]
        for f in fib:
            if f%M==0:
                divs.append(f)
        return divs

fibo=Fibonacci()
print(fibo.func1(100))
print(fibo.func2(100,7))
