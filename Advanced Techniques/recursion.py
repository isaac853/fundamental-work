import time


def fibonacci(n,np):
    print(n)
    time.sleep(0.1)
    tmp = np
    np = n
    n = n + tmp
    if n < 100000000:
        fibonacci(n,np)

# fibonacci(1,0)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(6))