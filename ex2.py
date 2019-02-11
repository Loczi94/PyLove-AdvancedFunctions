import time

def Fibonacci():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, b+a

for f in Fibonacci(): print(f); time.sleep(0.5)