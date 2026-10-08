def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("ingrese el numero que va a factorial: "))
    
if n<0:
    print("el numero debe ser mayor a cero")
else:
    resultado=factorial(n)
    
print("el factorial de ",n , " es",resultado)