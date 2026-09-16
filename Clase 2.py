def factorial(n):
    print("entrando con n=",n)
    if n==1:
        return 1
    return n * factorial(n-1)

factorial(5)