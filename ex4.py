
def Fibonacci(start, end):
    for i in range(start, end):
        if i == 0:
            prev1 = 0
        elif i == 1:
            prev2 = 1
            yield 1
        else:
            if (prev1+prev2)%2 == 1:
                yield prev1+prev2
            prev1, prev2 = prev2, prev1+prev2

fib = Fibonacci(0,100)
for f in fib:
    print(f)