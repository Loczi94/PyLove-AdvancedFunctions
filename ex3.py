
def Fibonacci(start, end):
    for i in range(start, end):
        if i == 0:
            prev1 = 0
            yield 0
        elif i == 1:
            prev2 = 1
            yield 1
        else:
            yield prev1+prev2
            prev1, prev2 = prev2, prev1+prev2

fib = Fibonacci(0,10)
for f in fib:
    print(f)